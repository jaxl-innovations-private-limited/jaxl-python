"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.kyc import Kyc
    from ..models.non_compliant_kyc_response import NonCompliantKycResponse


T = TypeVar("T", bound="NonCompliantKyc")


@attr.s(auto_attribs=True)
class NonCompliantKyc:
    """
    Attributes:
        kyc (Kyc): Adds a 'jaxlid' field which contains signed ID information.
        non_compliant_fields (List['NonCompliantKycResponse']):
    """

    kyc: "Kyc"
    non_compliant_fields: List["NonCompliantKycResponse"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kyc = self.kyc.to_dict()

        non_compliant_fields = []
        for non_compliant_fields_item_data in self.non_compliant_fields:
            non_compliant_fields_item = non_compliant_fields_item_data.to_dict()

            non_compliant_fields.append(non_compliant_fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kyc": kyc,
                "non_compliant_fields": non_compliant_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kyc import Kyc
        from ..models.non_compliant_kyc_response import NonCompliantKycResponse

        d = src_dict.copy()
        kyc = Kyc.from_dict(d.pop("kyc"))

        non_compliant_fields = []
        _non_compliant_fields = d.pop("non_compliant_fields")
        for non_compliant_fields_item_data in _non_compliant_fields:
            non_compliant_fields_item = NonCompliantKycResponse.from_dict(
                non_compliant_fields_item_data
            )

            non_compliant_fields.append(non_compliant_fields_item)

        non_compliant_kyc = cls(
            kyc=kyc,
            non_compliant_fields=non_compliant_fields,
        )

        non_compliant_kyc.additional_properties = d
        return non_compliant_kyc

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
