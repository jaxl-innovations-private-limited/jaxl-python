"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_transfer_rejected_errors import CallTransferRejectedErrors


T = TypeVar("T", bound="CallTransferRejected")


@attr.s(auto_attribs=True)
class CallTransferRejected:
    """The 400 body for `/v1/calls/{id}/transfer/`.

    Documents the `reason` the viewset now returns on every rejection
    path, so an integrator (and the generated SDK) can see that a 400
    carries an explanation instead of an empty body.

        Attributes:
            reason (str): Why the transfer was rejected.
            errors (Union[Unset, CallTransferRejectedErrors]): Per-field validation errors. Present only when the request
                body itself was invalid; `reason` summarises them.
    """

    reason: str
    errors: Union[Unset, "CallTransferRejectedErrors"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reason = self.reason
        errors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.call_transfer_rejected_errors import CallTransferRejectedErrors

        d = src_dict.copy()
        reason = d.pop("reason")

        _errors = d.pop("errors", UNSET)
        errors: Union[Unset, CallTransferRejectedErrors]
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = CallTransferRejectedErrors.from_dict(_errors)

        call_transfer_rejected = cls(
            reason=reason,
            errors=errors,
        )

        call_transfer_rejected.additional_properties = d
        return call_transfer_rejected

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
