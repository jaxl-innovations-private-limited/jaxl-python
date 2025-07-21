"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr


if TYPE_CHECKING:
    from ..models.proof_document import ProofDocument


T = TypeVar("T", bound="ProofsRequirement")


@attr.s(auto_attribs=True)
class ProofsRequirement:
    """
    Attributes:
        is_required (bool):
        documents (List['ProofDocument']):
    """

    is_required: bool
    documents: List["ProofDocument"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_required = self.is_required
        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()

            documents.append(documents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_required": is_required,
                "documents": documents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.proof_document import ProofDocument

        d = src_dict.copy()
        is_required = d.pop("is_required")

        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = ProofDocument.from_dict(documents_item_data)

            documents.append(documents_item)

        proofs_requirement = cls(
            is_required=is_required,
            documents=documents,
        )

        proofs_requirement.additional_properties = d
        return proofs_requirement

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
