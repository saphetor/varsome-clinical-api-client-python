from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Phenotype")


@attr.s(auto_attribs=True)
class Phenotype:
    """ """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    synonyms: Union[Unset, List[str]] = UNSET
    hpo_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        synonyms: Union[Unset, List[str]] = UNSET
        if not isinstance(self.synonyms, Unset):
            synonyms = self.synonyms

        hpo_id = self.hpo_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if synonyms is not UNSET:
            field_dict["synonyms"] = synonyms
        if hpo_id is not UNSET:
            field_dict["hpo_id"] = hpo_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        synonyms = cast(List[str], d.pop("synonyms", UNSET))

        hpo_id = d.pop("hpo_id", UNSET)

        phenotype = cls(
            id=id,
            name=name,
            synonyms=synonyms,
            hpo_id=hpo_id,
        )

        phenotype.additional_properties = d
        return phenotype

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
