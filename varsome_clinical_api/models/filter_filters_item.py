from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.filter_filters_item_filter_by import FilterFiltersItemFilterBy
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterFiltersItem")


@attr.s(auto_attribs=True)
class FilterFiltersItem:
    """ """

    name: str
    filter_by: Union[Unset, FilterFiltersItemFilterBy] = UNSET
    enabled: Union[Unset, bool] = UNSET
    exclude: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        filter_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_by, Unset):
            filter_by = self.filter_by.to_dict()

        enabled = self.enabled
        exclude = self.exclude

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if filter_by is not UNSET:
            field_dict["filter_by"] = filter_by
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if exclude is not UNSET:
            field_dict["exclude"] = exclude

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        _filter_by = d.pop("filter_by", UNSET)
        filter_by: Union[Unset, FilterFiltersItemFilterBy]
        if isinstance(_filter_by, Unset):
            filter_by = UNSET
        else:
            filter_by = FilterFiltersItemFilterBy.from_dict(_filter_by)

        enabled = d.pop("enabled", UNSET)

        exclude = d.pop("exclude", UNSET)

        filter_filters_item = cls(
            name=name,
            filter_by=filter_by,
            enabled=enabled,
            exclude=exclude,
        )

        filter_filters_item.additional_properties = d
        return filter_filters_item

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
