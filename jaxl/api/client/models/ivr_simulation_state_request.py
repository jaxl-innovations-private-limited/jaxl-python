"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr


T = TypeVar("T", bound="IVRSimulationStateRequest")


@attr.s(auto_attribs=True)
class IVRSimulationStateRequest:
    """
    Attributes:
        call_id (int):
        from_number (str):
        to_number (str):
    """

    call_id: int
    from_number: str
    to_number: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        call_id = self.call_id
        from_number = self.from_number
        to_number = self.to_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_id": call_id,
                "from_number": from_number,
                "to_number": to_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        call_id = d.pop("call_id")

        from_number = d.pop("from_number")

        to_number = d.pop("to_number")

        ivr_simulation_state_request = cls(
            call_id=call_id,
            from_number=from_number,
            to_number=to_number,
        )

        ivr_simulation_state_request.additional_properties = d
        return ivr_simulation_state_request

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
