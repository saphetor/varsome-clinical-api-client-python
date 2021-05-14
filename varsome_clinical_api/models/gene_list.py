import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeneList")


@attr.s(auto_attribs=True)
class GeneList:
    """ """

    name: str
    id: Union[Unset, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    last_update: Union[Unset, datetime.datetime] = UNSET
    comment: Union[Unset, str] = UNSET
    genes: Union[Unset, List[str]] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        is_public = self.is_public
        last_update: Union[Unset, str] = UNSET
        if not isinstance(self.last_update, Unset):
            last_update = self.last_update.isoformat()

        comment = self.comment
        genes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.genes, Unset):
            genes = self.genes

        user_name = self.user_name
        user_email = self.user_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if last_update is not UNSET:
            field_dict["last_update"] = last_update
        if comment is not UNSET:
            field_dict["comment"] = comment
        if genes is not UNSET:
            field_dict["genes"] = genes
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if user_email is not UNSET:
            field_dict["user_email"] = user_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        is_public = d.pop("is_public", UNSET)

        _last_update = d.pop("last_update", UNSET)
        last_update: Union[Unset, datetime.datetime]
        if isinstance(_last_update, Unset):
            last_update = UNSET
        else:
            last_update = isoparse(_last_update)

        comment = d.pop("comment", UNSET)

        genes = cast(List[str], d.pop("genes", UNSET))

        user_name = d.pop("user_name", UNSET)

        user_email = d.pop("user_email", UNSET)

        gene_list = cls(
            name=name,
            id=id,
            is_public=is_public,
            last_update=last_update,
            comment=comment,
            genes=genes,
            user_name=user_name,
            user_email=user_email,
        )

        gene_list.additional_properties = d
        return gene_list

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
