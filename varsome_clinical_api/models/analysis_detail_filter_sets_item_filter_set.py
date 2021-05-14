from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.analysis_detail_filter_sets_item_filter_set_filters_item import (
    AnalysisDetailFilterSetsItemFilterSetFiltersItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisDetailFilterSetsItemFilterSet")


@attr.s(auto_attribs=True)
class AnalysisDetailFilterSetsItemFilterSet:
    """ """

    name: str
    id: Union[Unset, str] = UNSET
    user_email: Union[Unset, str] = UNSET
    filters: Union[Unset, List[AnalysisDetailFilterSetsItemFilterSetFiltersItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        user_email = self.user_email
        filters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()

                filters.append(filters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        user_email = d.pop("user_email", UNSET)

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = AnalysisDetailFilterSetsItemFilterSetFiltersItem.from_dict(filters_item_data)

            filters.append(filters_item)

        analysis_detail_filter_sets_item_filter_set = cls(
            name=name,
            id=id,
            user_email=user_email,
            filters=filters,
        )

        analysis_detail_filter_sets_item_filter_set.additional_properties = d
        return analysis_detail_filter_sets_item_filter_set

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
