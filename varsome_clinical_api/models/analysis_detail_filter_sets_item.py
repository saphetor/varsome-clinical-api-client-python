from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.analysis_detail_filter_sets_item_filter_set import AnalysisDetailFilterSetsItemFilterSet

T = TypeVar("T", bound="AnalysisDetailFilterSetsItem")


@attr.s(auto_attribs=True)
class AnalysisDetailFilterSetsItem:
    """ """

    filter_set: AnalysisDetailFilterSetsItemFilterSet
    enabled: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_set = self.filter_set.to_dict()

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter_set": filter_set,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filter_set = AnalysisDetailFilterSetsItemFilterSet.from_dict(d.pop("filter_set"))

        enabled = d.pop("enabled")

        analysis_detail_filter_sets_item = cls(
            filter_set=filter_set,
            enabled=enabled,
        )

        analysis_detail_filter_sets_item.additional_properties = d
        return analysis_detail_filter_sets_item

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
