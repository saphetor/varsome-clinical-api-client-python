from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.analysis_results_annotations import AnalysisResultsAnnotations
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisResults")


@attr.s(auto_attribs=True)
class AnalysisResults:
    """ """

    variant_id: Union[Unset, int] = UNSET
    clinvar_class: Union[Unset, str] = UNSET
    allelic_balance: Union[Unset, float] = UNSET
    zygosity: Union[Unset, int] = UNSET
    coverage: Union[Unset, int] = UNSET
    variant_function: Union[Unset, str] = UNSET
    coding_impact: Union[Unset, str] = UNSET
    cgd_inheritance: Union[Unset, str] = UNSET
    genes: Union[Unset, str] = UNSET
    mt_prediction: Union[Unset, str] = UNSET
    min_sift_score: Union[Unset, float] = UNSET
    frequency: Union[Unset, float] = UNSET
    variant_class: Union[Unset, int] = UNSET
    annotations: Union[Unset, AnalysisResultsAnnotations] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        variant_id = self.variant_id
        clinvar_class = self.clinvar_class
        allelic_balance = self.allelic_balance
        zygosity = self.zygosity
        coverage = self.coverage
        variant_function = self.variant_function
        coding_impact = self.coding_impact
        cgd_inheritance = self.cgd_inheritance
        genes = self.genes
        mt_prediction = self.mt_prediction
        min_sift_score = self.min_sift_score
        frequency = self.frequency
        variant_class = self.variant_class
        annotations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id
        if clinvar_class is not UNSET:
            field_dict["clinvar_class"] = clinvar_class
        if allelic_balance is not UNSET:
            field_dict["allelic_balance"] = allelic_balance
        if zygosity is not UNSET:
            field_dict["zygosity"] = zygosity
        if coverage is not UNSET:
            field_dict["coverage"] = coverage
        if variant_function is not UNSET:
            field_dict["variant_function"] = variant_function
        if coding_impact is not UNSET:
            field_dict["coding_impact"] = coding_impact
        if cgd_inheritance is not UNSET:
            field_dict["cgd_inheritance"] = cgd_inheritance
        if genes is not UNSET:
            field_dict["genes"] = genes
        if mt_prediction is not UNSET:
            field_dict["mt_prediction"] = mt_prediction
        if min_sift_score is not UNSET:
            field_dict["min_sift_score"] = min_sift_score
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if variant_class is not UNSET:
            field_dict["variant_class"] = variant_class
        if annotations is not UNSET:
            field_dict["annotations"] = annotations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        variant_id = d.pop("variant_id", UNSET)

        clinvar_class = d.pop("clinvar_class", UNSET)

        allelic_balance = d.pop("allelic_balance", UNSET)

        zygosity = d.pop("zygosity", UNSET)

        coverage = d.pop("coverage", UNSET)

        variant_function = d.pop("variant_function", UNSET)

        coding_impact = d.pop("coding_impact", UNSET)

        cgd_inheritance = d.pop("cgd_inheritance", UNSET)

        genes = d.pop("genes", UNSET)

        mt_prediction = d.pop("mt_prediction", UNSET)

        min_sift_score = d.pop("min_sift_score", UNSET)

        frequency = d.pop("frequency", UNSET)

        variant_class = d.pop("variant_class", UNSET)

        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, AnalysisResultsAnnotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = AnalysisResultsAnnotations.from_dict(_annotations)

        analysis_results = cls(
            variant_id=variant_id,
            clinvar_class=clinvar_class,
            allelic_balance=allelic_balance,
            zygosity=zygosity,
            coverage=coverage,
            variant_function=variant_function,
            coding_impact=coding_impact,
            cgd_inheritance=cgd_inheritance,
            genes=genes,
            mt_prediction=mt_prediction,
            min_sift_score=min_sift_score,
            frequency=frequency,
            variant_class=variant_class,
            annotations=annotations,
        )

        analysis_results.additional_properties = d
        return analysis_results

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
