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
    from ..models.number_type import NumberType


T = TypeVar("T", bound="Inbound")


@attr.s(auto_attribs=True)
class Inbound:
    """
    Attributes:
        iso (str):
        country (str):
        country_code (int):
        local (Union[Unset, None, NumberType]):
        mobile (Union[Unset, None, NumberType]):
        toll_free (Union[Unset, None, NumberType]):
    """

    iso: str
    country: str
    country_code: int
    local: Union[Unset, None, "NumberType"] = UNSET
    mobile: Union[Unset, None, "NumberType"] = UNSET
    toll_free: Union[Unset, None, "NumberType"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        iso = self.iso
        country = self.country
        country_code = self.country_code
        local: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.local, Unset):
            local = self.local.to_dict() if self.local else None

        mobile: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.mobile, Unset):
            mobile = self.mobile.to_dict() if self.mobile else None

        toll_free: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.toll_free, Unset):
            toll_free = self.toll_free.to_dict() if self.toll_free else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iso": iso,
                "country": country,
                "country_code": country_code,
            }
        )
        if local is not UNSET:
            field_dict["local"] = local
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if toll_free is not UNSET:
            field_dict["toll_free"] = toll_free

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.number_type import NumberType

        d = src_dict.copy()
        iso = d.pop("iso")

        country = d.pop("country")

        country_code = d.pop("country_code")

        _local = d.pop("local", UNSET)
        local: Union[Unset, None, NumberType]
        if _local is None:
            local = None
        elif isinstance(_local, Unset):
            local = UNSET
        else:
            local = NumberType.from_dict(_local)

        _mobile = d.pop("mobile", UNSET)
        mobile: Union[Unset, None, NumberType]
        if _mobile is None:
            mobile = None
        elif isinstance(_mobile, Unset):
            mobile = UNSET
        else:
            mobile = NumberType.from_dict(_mobile)

        _toll_free = d.pop("toll_free", UNSET)
        toll_free: Union[Unset, None, NumberType]
        if _toll_free is None:
            toll_free = None
        elif isinstance(_toll_free, Unset):
            toll_free = UNSET
        else:
            toll_free = NumberType.from_dict(_toll_free)

        inbound = cls(
            iso=iso,
            country=country,
            country_code=country_code,
            local=local,
            mobile=mobile,
            toll_free=toll_free,
        )

        inbound.additional_properties = d
        return inbound

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
