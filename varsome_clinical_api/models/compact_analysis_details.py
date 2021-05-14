from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.compact_analysis_details_reference_genome import CompactAnalysisDetailsReferenceGenome
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompactAnalysisDetails")


@attr.s(auto_attribs=True)
class CompactAnalysisDetails:
    """ """

    analysis_id: int
    sample_id: int
    analysis_subject_id: str
    url: Union[Unset, str] = UNSET
    end_user_results_url: Union[Unset, str] = UNSET
    results_url: Union[Unset, str] = UNSET
    reference_genome: Union[Unset, CompactAnalysisDetailsReferenceGenome] = CompactAnalysisDetailsReferenceGenome.HG19
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        analysis_id = self.analysis_id
        sample_id = self.sample_id
        analysis_subject_id = self.analysis_subject_id
        url = self.url
        end_user_results_url = self.end_user_results_url
        results_url = self.results_url
        reference_genome: Union[Unset, str] = UNSET
        if not isinstance(self.reference_genome, Unset):
            reference_genome = self.reference_genome.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analysis_id": analysis_id,
                "sample_id": sample_id,
                "analysis_subject_id": analysis_subject_id,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if end_user_results_url is not UNSET:
            field_dict["end_user_results_url"] = end_user_results_url
        if results_url is not UNSET:
            field_dict["results_url"] = results_url
        if reference_genome is not UNSET:
            field_dict["reference_genome"] = reference_genome

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        analysis_id = d.pop("analysis_id")

        sample_id = d.pop("sample_id")

        analysis_subject_id = d.pop("analysis_subject_id")

        url = d.pop("url", UNSET)

        end_user_results_url = d.pop("end_user_results_url", UNSET)

        results_url = d.pop("results_url", UNSET)

        _reference_genome = d.pop("reference_genome", UNSET)
        reference_genome: Union[Unset, CompactAnalysisDetailsReferenceGenome]
        if isinstance(_reference_genome, Unset):
            reference_genome = UNSET
        else:
            reference_genome = CompactAnalysisDetailsReferenceGenome(_reference_genome)

        compact_analysis_details = cls(
            analysis_id=analysis_id,
            sample_id=sample_id,
            analysis_subject_id=analysis_subject_id,
            url=url,
            end_user_results_url=end_user_results_url,
            results_url=results_url,
            reference_genome=reference_genome,
        )

        compact_analysis_details.additional_properties = d
        return compact_analysis_details

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
