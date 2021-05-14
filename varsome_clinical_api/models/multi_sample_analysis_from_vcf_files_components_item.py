from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.multi_sample_analysis_from_vcf_files_components_item_affected_state import (
    MultiSampleAnalysisFromVCFFilesComponentsItemAffectedState,
)
from ..models.multi_sample_analysis_from_vcf_files_components_item_ethnicity import (
    MultiSampleAnalysisFromVCFFilesComponentsItemEthnicity,
)
from ..models.multi_sample_analysis_from_vcf_files_components_item_reference_genome import (
    MultiSampleAnalysisFromVCFFilesComponentsItemReferenceGenome,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiSampleAnalysisFromVCFFilesComponentsItem")


@attr.s(auto_attribs=True)
class MultiSampleAnalysisFromVCFFilesComponentsItem:
    """ """

    subject_id: str
    sample_file_ids: List[str]
    description: Union[Unset, str] = UNSET
    capture_kit_id: Union[Unset, int] = UNSET
    reference_genome: Union[
        Unset, MultiSampleAnalysisFromVCFFilesComponentsItemReferenceGenome
    ] = MultiSampleAnalysisFromVCFFilesComponentsItemReferenceGenome.HG19
    phenotype_ids: Union[Unset, List[str]] = UNSET
    disease_ids: Union[Unset, List[str]] = UNSET
    ethnicity: Union[Unset, MultiSampleAnalysisFromVCFFilesComponentsItemEthnicity] = UNSET
    sequencer: Union[Unset, str] = UNSET
    affected_state: Union[Unset, MultiSampleAnalysisFromVCFFilesComponentsItemAffectedState] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_id = self.subject_id
        sample_file_ids = self.sample_file_ids

        description = self.description
        capture_kit_id = self.capture_kit_id
        reference_genome: Union[Unset, str] = UNSET
        if not isinstance(self.reference_genome, Unset):
            reference_genome = self.reference_genome.value

        phenotype_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.phenotype_ids, Unset):
            phenotype_ids = self.phenotype_ids

        disease_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.disease_ids, Unset):
            disease_ids = self.disease_ids

        ethnicity: Union[Unset, str] = UNSET
        if not isinstance(self.ethnicity, Unset):
            ethnicity = self.ethnicity.value

        sequencer = self.sequencer
        affected_state: Union[Unset, str] = UNSET
        if not isinstance(self.affected_state, Unset):
            affected_state = self.affected_state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject_id": subject_id,
                "sample_file_ids": sample_file_ids,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if capture_kit_id is not UNSET:
            field_dict["capture_kit_id"] = capture_kit_id
        if reference_genome is not UNSET:
            field_dict["reference_genome"] = reference_genome
        if phenotype_ids is not UNSET:
            field_dict["phenotype_ids"] = phenotype_ids
        if disease_ids is not UNSET:
            field_dict["disease_ids"] = disease_ids
        if ethnicity is not UNSET:
            field_dict["ethnicity"] = ethnicity
        if sequencer is not UNSET:
            field_dict["sequencer"] = sequencer
        if affected_state is not UNSET:
            field_dict["affected_state"] = affected_state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_id = d.pop("subject_id")

        sample_file_ids = cast(List[str], d.pop("sample_file_ids"))

        description = d.pop("description", UNSET)

        capture_kit_id = d.pop("capture_kit_id", UNSET)

        _reference_genome = d.pop("reference_genome", UNSET)
        reference_genome: Union[Unset, MultiSampleAnalysisFromVCFFilesComponentsItemReferenceGenome]
        if isinstance(_reference_genome, Unset):
            reference_genome = UNSET
        else:
            reference_genome = MultiSampleAnalysisFromVCFFilesComponentsItemReferenceGenome(_reference_genome)

        phenotype_ids = cast(List[str], d.pop("phenotype_ids", UNSET))

        disease_ids = cast(List[str], d.pop("disease_ids", UNSET))

        _ethnicity = d.pop("ethnicity", UNSET)
        ethnicity: Union[Unset, MultiSampleAnalysisFromVCFFilesComponentsItemEthnicity]
        if isinstance(_ethnicity, Unset):
            ethnicity = UNSET
        else:
            ethnicity = MultiSampleAnalysisFromVCFFilesComponentsItemEthnicity(_ethnicity)

        sequencer = d.pop("sequencer", UNSET)

        _affected_state = d.pop("affected_state", UNSET)
        affected_state: Union[Unset, MultiSampleAnalysisFromVCFFilesComponentsItemAffectedState]
        if isinstance(_affected_state, Unset):
            affected_state = UNSET
        else:
            affected_state = MultiSampleAnalysisFromVCFFilesComponentsItemAffectedState(_affected_state)

        multi_sample_analysis_from_vcf_files_components_item = cls(
            subject_id=subject_id,
            sample_file_ids=sample_file_ids,
            description=description,
            capture_kit_id=capture_kit_id,
            reference_genome=reference_genome,
            phenotype_ids=phenotype_ids,
            disease_ids=disease_ids,
            ethnicity=ethnicity,
            sequencer=sequencer,
            affected_state=affected_state,
        )

        multi_sample_analysis_from_vcf_files_components_item.additional_properties = d
        return multi_sample_analysis_from_vcf_files_components_item

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
