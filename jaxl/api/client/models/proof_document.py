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
    from ..models.proof_field import ProofField


T = TypeVar("T", bound="ProofDocument")


@attr.s(auto_attribs=True)
class ProofDocument:
    """
    Attributes:
        name (str):
        title (str):
        requirement (str):
        proof_fields (List['ProofField']):
        description (Union[Unset, None, str]):
    """

    name: str
    title: str
    requirement: str
    proof_fields: List["ProofField"]
    description: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        title = self.title
        requirement = self.requirement
        proof_fields = []
        for proof_fields_item_data in self.proof_fields:
            proof_fields_item = proof_fields_item_data.to_dict()

            proof_fields.append(proof_fields_item)

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "title": title,
                "requirement": requirement,
                "proof_fields": proof_fields,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.proof_field import ProofField

        d = src_dict.copy()
        name = d.pop("name")

        title = d.pop("title")

        requirement = d.pop("requirement")

        proof_fields = []
        _proof_fields = d.pop("proof_fields")
        for proof_fields_item_data in _proof_fields:
            proof_fields_item = ProofField.from_dict(proof_fields_item_data)

            proof_fields.append(proof_fields_item)

        description = d.pop("description", UNSET)

        proof_document = cls(
            name=name,
            title=title,
            requirement=requirement,
            proof_fields=proof_fields,
            description=description,
        )

        proof_document.additional_properties = d
        return proof_document

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
