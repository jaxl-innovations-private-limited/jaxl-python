"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.inbound import Inbound
    from ..models.outbound import Outbound


T = TypeVar("T", bound="PricingResponse")


@attr.s(auto_attribs=True)
class PricingResponse:
    """
    Attributes:
        outbound (List['Outbound']):
        inbound (List['Inbound']):
    """

    outbound: List["Outbound"]
    inbound: List["Inbound"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        outbound = []
        for outbound_item_data in self.outbound:
            outbound_item = outbound_item_data.to_dict()

            outbound.append(outbound_item)

        inbound = []
        for inbound_item_data in self.inbound:
            inbound_item = inbound_item_data.to_dict()

            inbound.append(inbound_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outbound": outbound,
                "inbound": inbound,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inbound import Inbound
        from ..models.outbound import Outbound

        d = src_dict.copy()
        outbound = []
        _outbound = d.pop("outbound")
        for outbound_item_data in _outbound:
            outbound_item = Outbound.from_dict(outbound_item_data)

            outbound.append(outbound_item)

        inbound = []
        _inbound = d.pop("inbound")
        for inbound_item_data in _inbound:
            inbound_item = Inbound.from_dict(inbound_item_data)

            inbound.append(inbound_item)

        pricing_response = cls(
            outbound=outbound,
            inbound=inbound,
        )

        pricing_response.additional_properties = d
        return pricing_response

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
