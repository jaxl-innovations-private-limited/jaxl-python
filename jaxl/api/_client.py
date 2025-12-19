"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import base64
import functools
import getpass
import json
import logging
import os
import pathlib
import platform as pyplatform
import socket
import time
import uuid
from datetime import datetime, timedelta, timezone
from enum import Enum
from http import HTTPStatus
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    TypedDict,
    TypeVar,
    Union,
    cast,
)

import jwt
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

from jaxl.api.client import Client
from jaxl.api.client.api.v1 import v1_devices_attest_create
from jaxl.api.client.client import AuthenticatedClient
from jaxl.api.client.models.device_attestation_response import (
    DeviceAttestationResponse,
)
from jaxl.api.client.types import Response


logger = logging.getLogger(__name__)

DEFAULT_ISSUER = "jaxl"
DEFAULT_AUDIENCE = "dialer"
JAXL_CONTAINER_USER = "jaxl-python"


class ApiCredentialsWatermark(TypedDict):
    """ApiCredentialsWatermark"""

    version: int
    env: str
    by: int
    on: str
    via: str
    through: str


class ApiCredentialsAppPlatforms(TypedDict):
    """ApiCredentialsAppPlatforms"""

    ios: Optional[str]
    android: Optional[str]
    domain: Optional[str]


class ApiCredentialsApp(TypedDict):
    """ApiCredentialsApp"""

    id: int
    type: int
    platforms: ApiCredentialsAppPlatforms


class ApiCredentialsClient(TypedDict):
    """ApiCredentialsClient"""

    key: str
    secret: str
    genesis_key: str
    platform: int


class ApiCredentials(TypedDict):
    """ApiCredentials"""

    watermark: ApiCredentialsWatermark
    app: ApiCredentialsApp
    client: ApiCredentialsClient
    servers: List[str]


class JwtMessage(TypedDict):
    """JwtMessage"""

    version: str
    env: str
    signature: str
    me: str
    now: str
    servers: List[str]
    device_id: Optional[int]
    app_version: Optional[str]


class TokenSignatureMessage(TypedDict):
    """TokenSignatureMessage"""

    version: int
    env: str
    app_id: int
    me: str
    now: str
    device_id: Optional[int]
    app_version: Optional[str]


@functools.cache
def default_api_credentials() -> ApiCredentials:
    """Reads JAXL_API_CREDENTIALS file and return json credentials."""
    path = os.environ.get("JAXL_API_CREDENTIALS")
    if path is None:
        raise ValueError("JAXL_API_CREDENTIALS environment variable is required.")
    return cast(  # pragma: no cover
        ApiCredentials,
        json.loads(Path(path).read_text("utf-8")),
    )


@functools.cache
def get_system_identity() -> str:
    """Returns username@hostname identity of the system."""
    #
    # 2023-09-30T02:43:36.033347Z identity = f"{getpass.getuser()}@{socket.gethostname()}"
    # 2023-09-30T02:43:36.033353Z ^^^^^^^^^^^^^^^^^
    # 2023-09-30T02:43:36.033357Z File "/usr/local/lib/python3.11/getpass.py", line 169, in getuser
    # 2023-09-30T02:43:36.033362Z return pwd.getpwuid(os.getuid())[0]
    # 2023-09-30T02:43:36.033366Z ^^^^^^^^^^^^^^^^^^^^^^^^^
    # 2023-09-30T02:43:36.033371Z KeyError: 'getpwuid(): uid not found: 0'
    #
    # ^^^^ BECAUSE WE HAVE SEEN ERRORS LIVE ABOVE
    # USE A DEFAULT USERNAME, HOSTNAME FOR SCENARIOS
    # WHEN WE ARE UNABLE TO GET THESE DETAILS FROM
    # THE UNDERLYING OPERATING SYSTEM.
    #
    username = "jaxl"
    try:
        username = os.environ.get(
            "USER",
            (
                os.environ.get("JAXL_CONTAINER_USER", JAXL_CONTAINER_USER)
                if Path("/.dockerenv").is_file()
                else getpass.getuser()
            ),
        )

    except Exception:  # pylint: disable=broad-exception-caught
        pass
    hostname = "api.frontend"
    try:
        hostname = socket.gethostname()
    except Exception:  # pylint: disable=broad-exception-caught
        pass
    return f"{username}@{hostname}"


def generate_signature(privkey: bytes, message: bytes) -> bytes:
    """sign messaging using our priv key"""
    return cast(
        rsa.RSAPrivateKey,
        serialization.load_pem_private_key(
            privkey,
            backend=default_backend(),
            password=None,
        ),
    ).sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )


def encode(
    payload: Dict[str, Any],
    private_key: str,
    expires_at: Optional[datetime] = None,
    valid_since: Optional[datetime] = None,
    audience: str = DEFAULT_AUDIENCE,
) -> str:
    """Encode JWT parameters"""
    copy = payload.copy()
    copy["iss"] = DEFAULT_ISSUER
    copy["aud"] = audience
    copy["iat"] = datetime.now(tz=timezone.utc)
    if expires_at is not None:
        copy["exp"] = expires_at
    if valid_since is not None:
        copy["nbf"] = valid_since
    return jwt.encode(copy, key=private_key, algorithm="RS256")


def generate_api_token(
    credentials: ApiCredentials,
    ttl: int,
    device_id: Optional[int] = None,
    app_version: Optional[str] = None,
) -> str:
    """Generates an api token"""
    now = datetime.now(tz=timezone.utc)
    identity = get_system_identity()
    signature = base64.b64encode(
        generate_signature(
            privkey=credentials["client"]["secret"].encode(),
            message=json.dumps(
                TokenSignatureMessage(
                    version=credentials["watermark"]["version"],
                    env=credentials["watermark"]["env"],
                    app_id=credentials["app"]["id"],
                    me=identity,
                    now=str(now),
                    device_id=device_id,
                    app_version=app_version,
                )
            ).encode(),
        )
    ).decode()
    return encode(
        payload=cast(
            Dict[str, Any],
            JwtMessage(
                version=str(credentials["watermark"]["version"]),
                env=credentials["watermark"]["env"],
                signature=signature,
                me=identity,
                now=str(now),
                servers=credentials["servers"],
                device_id=device_id,
                app_version=app_version,
            ),
        ),
        private_key=credentials["client"]["secret"],
        valid_since=now,
        expires_at=now + timedelta(seconds=ttl),
    )


def attest() -> Optional[Dict[str, Any]]:
    """Ensures valid attestation with Jaxl backend.

    - If attestation already exists, reuses it.
    - Stores attestation in ~/.jaxl/api/attestation.json encrypted using api client genesis key.
    """
    data_dir = os.path.join(str(pathlib.Path.home()), ".jaxl", "api")
    os.makedirs(data_dir, exist_ok=True)
    attestation_path = Path(data_dir) / os.environ.get(
        "JAXL_ATTESTATION_FILE_NAME", "attestation.json"
    )
    if attestation_path.exists():
        return cast(Dict[str, Any], json.loads(attestation_path.read_text()))
    attestation = _attest()
    if attestation is not None:
        attestation_path.write_text(json.dumps(attestation))
    return attestation


def _attest() -> Optional[Dict[str, Any]]:
    """Ensures valid attestation with Jaxl backend."""
    sk = default_api_credentials()["client"]["genesis_key"]
    idd = None
    did = f"jaxl:sdk:{uuid.uuid4().hex}"
    origin = f"{pyplatform.system().lower()}://"
    ip_address = "127.0.0.1"

    response = JaxlApiClient.attest(
        _api_root(JaxlApiModule.ACCOUNT),
        key=sk,
        device_id=did,
        device_pk=idd,
        origin=origin,
        ip_address=ip_address,
        platform=3,
    )
    if isinstance(response, int):
        return None
    return response


def encrypt(text: str) -> str:
    attestation = attest()
    assert attestation and "sk" in attestation
    return (
        Fernet(attestation["sk"])
        .encrypt(json.dumps(text).encode("utf-8"))
        .decode("utf-8")
    )


class JaxlApiModule(Enum):
    """Available API Modules"""

    ACCOUNT = 1
    CALL = 2
    MESSAGE = 3
    NOTIFICATION = 4
    PAYMENT = 5


def jaxl_api_client(
    module: JaxlApiModule,
    credentials: Optional[ApiCredentials] = None,
    auth_token: Optional[str] = None,
    set_org_id: bool = True,
) -> "AuthenticatedClient":
    """Returns JaxlApiClient with auth token and device id preset."""
    attestation = attest()
    auth_token = auth_token or os.environ.get("JAXL_API_AUTH_TOKEN", None)
    client = JaxlApiClient(_api_root(module), credentials=credentials)
    assert attestation is not None, "Missing attestation"
    assert auth_token is not None, "Missing JAXL_API_AUTH_TOKEN"
    client.set_device_id(attestation["id"])
    client.set_auth_token(auth_token)
    if set_org_id:
        from jaxl.api.resources.orgs import first_org_id

        client.set_org_id(first_org_id())
    return cast(AuthenticatedClient, client)


# pylint: disable=too-many-return-statements,too-many-branches
def _api_root(module: JaxlApiModule) -> str:
    """Returns API root for given API Module."""
    env = default_api_credentials()["watermark"]["env"]
    if module == JaxlApiModule.ACCOUNT:
        if env == "production":
            return "https://fin.jaxl.com"
        if env == "staging":
            return "https://payments.jaxl.app"
        if env == "run":
            return "https://pay.jaxl.run"
        if env == "dev":
            return os.environ["JAXL_ACCOUNT_API_ROOT"]
    if module == JaxlApiModule.PAYMENT:
        if env == "production":
            return "https://fin.jaxl.com"
        if env == "staging":
            return "https://payments.jaxl.app"
        if env == "run":
            return "https://pay.jaxl.run"
        if env == "dev":
            return os.environ["JAXL_PAYMENT_API_ROOT"]
    if module == JaxlApiModule.CALL:
        if env == "production":
            return "https://live.jaxl.com"
        if env == "staging":
            return "https://transport.jaxl.app"
        if env == "run":
            return "https://ws.jaxl.run"
        if env == "dev":
            return os.environ["JAXL_CALL_API_ROOT"]
    if module == JaxlApiModule.MESSAGE:
        if env == "production":
            return "https://fin.jaxl.com"
        if env == "staging":
            return "https://payments.jaxl.app"
        if env == "run":
            return "https://pay.jaxl.run"
        if env == "dev":
            return os.environ["JAXL_MESSAGE_API_ROOT"]
    raise NotImplementedError()


# pylint: disable=too-many-instance-attributes
class JaxlApiClient(Client):
    """Api client which automatically attaches outgoing api keys
    using JAXL_API_CREDENTIALS environment variable."""

    def __init__(
        self,
        *args: Any,
        audience: str = DEFAULT_AUDIENCE,
        platform: int = 3,  # 3 = CLI
        credentials: Optional[ApiCredentials] = None,
        **kwargs: Any,
    ) -> None:
        self.audience = audience
        self.credentials: ApiCredentials = credentials or default_api_credentials()
        self.device_id: Optional[int] = None
        self.org_id: Optional[int] = None
        self.auth_token: Optional[str] = None
        self.platform: int = platform
        super().__init__(*args, **kwargs)

    # pylint: disable=too-many-arguments,too-many-positional-arguments
    @staticmethod
    def attest(
        api_root: str,
        key: str,
        device_id: str,
        device_pk: Optional[int],
        origin: str,
        ip_address: str,
        signed_user_cookie: Optional[str] = None,
        platform: Optional[int] = 3,
    ) -> Union[int, Dict[str, Any]]:
        """Performs attestation and return decrypted payload.

        Either returns decrypted payload (a dictionary) or
        will return HTTP status code in case of API errors.

        1000 is a reserved status code for cases when API
        status is success but we are unable to parse response.

        1001 is a reserved status code for cases when API
        status is success but we are unable to decrypt the
        parsed response.
        """
        response = JaxlApiClient.hit_attest(
            api_root=api_root,
            key=key,
            device_id=device_id,
            device_pk=device_pk,
            origin=origin,
            ip_address=ip_address,
            signed_user_cookie=signed_user_cookie,
            platform=platform,
        )
        if response.status_code == HTTPStatus.OK:
            if response.parsed is None:
                return 1000
            fernet = Fernet(key)
            try:
                return cast(
                    Dict[str, Any],
                    json.loads(fernet.decrypt(response.parsed.encrypted.encode())),
                )
            except InvalidToken:
                return 1001
        return response.status_code

    # pylint: disable=too-many-arguments
    @staticmethod
    def hit_attest(
        api_root: str,
        key: str,
        device_id: str,
        device_pk: Optional[int],
        origin: str,
        ip_address: str,
        signed_user_cookie: Optional[str] = None,
        platform: Optional[int] = 3,
    ) -> Response[Union[Any, DeviceAttestationResponse]]:
        """Performs attestation process and returns secret key to use
        for establishing transport connection.

        For first time devices, genesis attestation key is used.
        For revisiting devices, previously exchanged attestation key is used.

        Attestation keys are stored in user session data.
        On frontend, session cookie helps to identify
        first time vs revisiting users.
        """
        assert platform
        fernet = Fernet(key)
        return ensure(
            api_root,
            headers={
                "origin": origin,
                "x-forwarded-for": ip_address,
                "x-device-attest": fernet.encrypt(
                    json.dumps(
                        {
                            "pd": device_id,
                            # TODO: Send a signature from frontend as device token
                            # which can be verified by our backend, by calling frontend's
                            # backend service.
                            "dt": "",
                            "cookie": signed_user_cookie,
                        }
                    ).encode("utf-8")
                ).decode("utf-8"),
                "x-device-id": device_id,
            },
            client_kwargs={"platform": platform},
            session={"idd": device_pk},
            func=v1_devices_attest_create.sync_detailed,
        )

    def set_device_id(self, device_id: Optional[int]) -> None:
        """Set a device ID identity for outgoing requests."""
        self.device_id = device_id

    def set_org_id(self, org_id: Optional[int]) -> None:
        """Set org ID when making requests for a B2B application."""
        if self.credentials["app"]["type"] != 2:
            raise ValueError("Org ID can only be set for B2B apps")
        self.org_id = org_id

    def set_auth_token(self, auth_token: str) -> None:
        """Set authentication token"""
        assert self.platform == 3
        self.auth_token = auth_token

    def get_headers(self) -> Dict[str, str]:
        """Prepare headers"""
        jaxl_headers = {
            "X-JAXL-PLATFORM": str(self.platform),
            "X-JAXL-API-KEY": f"{self.credentials['client']['key']}",
            "X-JAXL-API-TOKEN": generate_api_token(
                self.credentials,
                ttl=int(os.environ.get("JAXL_API_TOKEN_EXPIRY_IN_SEC", 30)),
                device_id=self.device_id,
            ),
            "X-JAXL-CLIENT-EP": str(int(time.time() * 1000)),
        }
        if self.org_id is not None:
            jaxl_headers["X-JAXL-ORGID"] = str(self.org_id)
        if self.auth_token is not None:
            jaxl_headers["X-JAXL-AUTH-TOKEN"] = self.auth_token
        return {
            **super().get_headers(),
            **jaxl_headers,
        }

    def get_timeout(self) -> float:
        """Server can take upto 5-7sec to startup on Cloud Run,
        use a timeout of 10-seconds."""
        return 10.0


T = TypeVar("T")


# pylint: disable=too-many-arguments
def _ensure(
    api_root: str,
    headers: Dict[str, str],
    session: Dict[str, Any],
    func: Callable[..., Response[T]],
    client_kwargs: Any = None,
    **kwargs: Any,
) -> Response[T]:
    client = JaxlApiClient(
        api_root,
        headers=headers,
        **(client_kwargs or {}),
    )
    if session.get("idd", None) is not None:
        client.set_device_id(session["idd"])
    if session.get("org_id", None) is not None and client.credentials["app"][
        "type"
    ] in (2, 3):
        client.set_org_id(session["org_id"])
    return func(client=cast(AuthenticatedClient, client), **kwargs)


# pylint: disable=too-many-arguments,too-many-positional-arguments
def ensure(
    api_root: str,
    headers: Dict[str, str],
    session: Dict[str, Any],
    func: Callable[..., Response[T]],
    client_kwargs: Any = None,
    **kwargs: Any,
) -> Response[T]:
    """Automatically retry Jaxl API Requests."""
    max_tries: int = 5
    min_retry_after: int = 1
    max_retry_after: int = 10
    total_tries = 0
    while total_tries < max_tries:
        response = _ensure(
            api_root,
            headers=headers,
            session=session,
            func=func,
            client_kwargs=client_kwargs,
            # client_request=client_request,
            **kwargs,
        )
        if response.status_code not in (502, 503, 504):
            break
        # Retry when status code is 502, 503, 504
        retry_in = min(
            min_retry_after + pow(2, total_tries % (max_tries + 1)),
            max_retry_after,
        )
        # pylint: disable=logging-not-lazy
        logger.info(
            f"[ensure] {func.__module__}.{func.__name__} failed "
            + f"with status code {response.status_code}, "
            + f"retrying in {retry_in} seconds"
        )
        time.sleep(retry_in)
        total_tries += 1
    return response
