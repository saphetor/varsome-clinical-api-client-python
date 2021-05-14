import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.analysis_detail_analysis_info import AnalysisDetailAnalysisInfo
from ..models.analysis_detail_analysis_state import AnalysisDetailAnalysisState
from ..models.analysis_detail_annotation_databases_item import AnalysisDetailAnnotationDatabasesItem
from ..models.analysis_detail_capture_kit import AnalysisDetailCaptureKit
from ..models.analysis_detail_ethnicity import AnalysisDetailEthnicity
from ..models.analysis_detail_filter_sets_item import AnalysisDetailFilterSetsItem
from ..models.analysis_detail_phenotypes_item import AnalysisDetailPhenotypesItem
from ..models.analysis_detail_reference_genome import AnalysisDetailReferenceGenome
from ..models.analysis_detail_sample_type import AnalysisDetailSampleType
from ..models.analysis_detail_selected_variants_item import AnalysisDetailSelectedVariantsItem
from ..models.analysis_detail_variants_to_keep import AnalysisDetailVariantsToKeep
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisDetail")


@attr.s(auto_attribs=True)
class AnalysisDetail:
    """ """

    subject_id: str
    analysis_id: Union[Unset, int] = UNSET
    sample_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    capture_kit: Union[Unset, AnalysisDetailCaptureKit] = AnalysisDetailCaptureKit.VALUE_35000000
    sequencer: Union[Unset, str] = "Illumina"
    sample_type: Union[Unset, AnalysisDetailSampleType] = AnalysisDetailSampleType.GERMLINE
    url: Union[Unset, str] = UNSET
    analysis_state: Union[Unset, AnalysisDetailAnalysisState] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    user_email: Union[Unset, str] = UNSET
    user_full_name: Union[Unset, str] = UNSET
    reference_genome: Union[Unset, AnalysisDetailReferenceGenome] = AnalysisDetailReferenceGenome.HG19
    variants_to_keep: Union[Unset, AnalysisDetailVariantsToKeep] = AnalysisDetailVariantsToKeep.PASS_ONLY
    review_url: Union[Unset, str] = UNSET
    end_user_results_url: Union[Unset, str] = UNSET
    results_url: Union[Unset, str] = UNSET
    annotated_vcf_url: Union[Unset, str] = UNSET
    quality_control_report_url: Union[Unset, str] = UNSET
    results_count: Union[Unset, int] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    analysis_type: Union[Unset, str] = "F"
    phenotypes: Union[Unset, List[AnalysisDetailPhenotypesItem]] = UNSET
    diseases: Union[Unset, List[str]] = UNSET
    analysis_subject_id: Union[Unset, str] = UNSET
    pipeline_finished: Union[Unset, bool] = UNSET
    pipeline_failed: Union[Unset, bool] = UNSET
    pipeline_progress: Union[Unset, bool] = UNSET
    visible_to_user: Union[Unset, bool] = UNSET
    selected_variants_url: Union[Unset, str] = UNSET
    analysis_info: Union[Unset, AnalysisDetailAnalysisInfo] = UNSET
    ethnicity: Union[Unset, AnalysisDetailEthnicity] = UNSET
    annotation_databases: Union[Unset, List[AnalysisDetailAnnotationDatabasesItem]] = UNSET
    filter_sets: Union[Unset, List[AnalysisDetailFilterSetsItem]] = UNSET
    selected_variants: Union[Unset, List[AnalysisDetailSelectedVariantsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_id = self.subject_id
        analysis_id = self.analysis_id
        sample_id = self.sample_id
        description = self.description
        capture_kit: Union[Unset, int] = UNSET
        if not isinstance(self.capture_kit, Unset):
            capture_kit = self.capture_kit.value

        sequencer = self.sequencer
        sample_type: Union[Unset, str] = UNSET
        if not isinstance(self.sample_type, Unset):
            sample_type = self.sample_type.value

        url = self.url
        analysis_state: Union[Unset, str] = UNSET
        if not isinstance(self.analysis_state, Unset):
            analysis_state = self.analysis_state.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        user_email = self.user_email
        user_full_name = self.user_full_name
        reference_genome: Union[Unset, str] = UNSET
        if not isinstance(self.reference_genome, Unset):
            reference_genome = self.reference_genome.value

        variants_to_keep: Union[Unset, str] = UNSET
        if not isinstance(self.variants_to_keep, Unset):
            variants_to_keep = self.variants_to_keep.value

        review_url = self.review_url
        end_user_results_url = self.end_user_results_url
        results_url = self.results_url
        annotated_vcf_url = self.annotated_vcf_url
        quality_control_report_url = self.quality_control_report_url
        results_count = self.results_count
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        analysis_type = self.analysis_type
        phenotypes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.phenotypes, Unset):
            phenotypes = []
            for phenotypes_item_data in self.phenotypes:
                phenotypes_item = phenotypes_item_data.to_dict()

                phenotypes.append(phenotypes_item)

        diseases: Union[Unset, List[str]] = UNSET
        if not isinstance(self.diseases, Unset):
            diseases = self.diseases

        analysis_subject_id = self.analysis_subject_id
        pipeline_finished = self.pipeline_finished
        pipeline_failed = self.pipeline_failed
        pipeline_progress = self.pipeline_progress
        visible_to_user = self.visible_to_user
        selected_variants_url = self.selected_variants_url
        analysis_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.analysis_info, Unset):
            analysis_info = self.analysis_info.to_dict()

        ethnicity: Union[Unset, str] = UNSET
        if not isinstance(self.ethnicity, Unset):
            ethnicity = self.ethnicity.value

        annotation_databases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.annotation_databases, Unset):
            annotation_databases = []
            for annotation_databases_item_data in self.annotation_databases:
                annotation_databases_item = annotation_databases_item_data.to_dict()

                annotation_databases.append(annotation_databases_item)

        filter_sets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filter_sets, Unset):
            filter_sets = []
            for filter_sets_item_data in self.filter_sets:
                filter_sets_item = filter_sets_item_data.to_dict()

                filter_sets.append(filter_sets_item)

        selected_variants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.selected_variants, Unset):
            selected_variants = []
            for selected_variants_item_data in self.selected_variants:
                selected_variants_item = selected_variants_item_data.to_dict()

                selected_variants.append(selected_variants_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject_id": subject_id,
            }
        )
        if analysis_id is not UNSET:
            field_dict["analysis_id"] = analysis_id
        if sample_id is not UNSET:
            field_dict["sample_id"] = sample_id
        if description is not UNSET:
            field_dict["description"] = description
        if capture_kit is not UNSET:
            field_dict["capture_kit"] = capture_kit
        if sequencer is not UNSET:
            field_dict["sequencer"] = sequencer
        if sample_type is not UNSET:
            field_dict["sample_type"] = sample_type
        if url is not UNSET:
            field_dict["url"] = url
        if analysis_state is not UNSET:
            field_dict["analysis_state"] = analysis_state
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if user_full_name is not UNSET:
            field_dict["user_full_name"] = user_full_name
        if reference_genome is not UNSET:
            field_dict["reference_genome"] = reference_genome
        if variants_to_keep is not UNSET:
            field_dict["variants_to_keep"] = variants_to_keep
        if review_url is not UNSET:
            field_dict["review_url"] = review_url
        if end_user_results_url is not UNSET:
            field_dict["end_user_results_url"] = end_user_results_url
        if results_url is not UNSET:
            field_dict["results_url"] = results_url
        if annotated_vcf_url is not UNSET:
            field_dict["annotated_vcf_url"] = annotated_vcf_url
        if quality_control_report_url is not UNSET:
            field_dict["quality_control_report_url"] = quality_control_report_url
        if results_count is not UNSET:
            field_dict["results_count"] = results_count
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if analysis_type is not UNSET:
            field_dict["analysis_type"] = analysis_type
        if phenotypes is not UNSET:
            field_dict["phenotypes"] = phenotypes
        if diseases is not UNSET:
            field_dict["diseases"] = diseases
        if analysis_subject_id is not UNSET:
            field_dict["analysis_subject_id"] = analysis_subject_id
        if pipeline_finished is not UNSET:
            field_dict["pipeline_finished"] = pipeline_finished
        if pipeline_failed is not UNSET:
            field_dict["pipeline_failed"] = pipeline_failed
        if pipeline_progress is not UNSET:
            field_dict["pipeline_progress"] = pipeline_progress
        if visible_to_user is not UNSET:
            field_dict["visible_to_user"] = visible_to_user
        if selected_variants_url is not UNSET:
            field_dict["selected_variants_url"] = selected_variants_url
        if analysis_info is not UNSET:
            field_dict["analysis_info"] = analysis_info
        if ethnicity is not UNSET:
            field_dict["ethnicity"] = ethnicity
        if annotation_databases is not UNSET:
            field_dict["annotation_databases"] = annotation_databases
        if filter_sets is not UNSET:
            field_dict["filter_sets"] = filter_sets
        if selected_variants is not UNSET:
            field_dict["selected_variants"] = selected_variants

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_id = d.pop("subject_id")

        analysis_id = d.pop("analysis_id", UNSET)

        sample_id = d.pop("sample_id", UNSET)

        description = d.pop("description", UNSET)

        _capture_kit = d.pop("capture_kit", UNSET)
        capture_kit: Union[Unset, AnalysisDetailCaptureKit]
        if isinstance(_capture_kit, Unset):
            capture_kit = UNSET
        else:
            capture_kit = AnalysisDetailCaptureKit(_capture_kit)

        sequencer = d.pop("sequencer", UNSET)

        _sample_type = d.pop("sample_type", UNSET)
        sample_type: Union[Unset, AnalysisDetailSampleType]
        if isinstance(_sample_type, Unset):
            sample_type = UNSET
        else:
            sample_type = AnalysisDetailSampleType(_sample_type)

        url = d.pop("url", UNSET)

        _analysis_state = d.pop("analysis_state", UNSET)
        analysis_state: Union[Unset, AnalysisDetailAnalysisState]
        if isinstance(_analysis_state, Unset):
            analysis_state = UNSET
        else:
            analysis_state = AnalysisDetailAnalysisState(_analysis_state)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        user_email = d.pop("user_email", UNSET)

        user_full_name = d.pop("user_full_name", UNSET)

        _reference_genome = d.pop("reference_genome", UNSET)
        reference_genome: Union[Unset, AnalysisDetailReferenceGenome]
        if isinstance(_reference_genome, Unset):
            reference_genome = UNSET
        else:
            reference_genome = AnalysisDetailReferenceGenome(_reference_genome)

        _variants_to_keep = d.pop("variants_to_keep", UNSET)
        variants_to_keep: Union[Unset, AnalysisDetailVariantsToKeep]
        if isinstance(_variants_to_keep, Unset):
            variants_to_keep = UNSET
        else:
            variants_to_keep = AnalysisDetailVariantsToKeep(_variants_to_keep)

        review_url = d.pop("review_url", UNSET)

        end_user_results_url = d.pop("end_user_results_url", UNSET)

        results_url = d.pop("results_url", UNSET)

        annotated_vcf_url = d.pop("annotated_vcf_url", UNSET)

        quality_control_report_url = d.pop("quality_control_report_url", UNSET)

        results_count = d.pop("results_count", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        analysis_type = d.pop("analysis_type", UNSET)

        phenotypes = []
        _phenotypes = d.pop("phenotypes", UNSET)
        for phenotypes_item_data in _phenotypes or []:
            phenotypes_item = AnalysisDetailPhenotypesItem.from_dict(phenotypes_item_data)

            phenotypes.append(phenotypes_item)

        diseases = cast(List[str], d.pop("diseases", UNSET))

        analysis_subject_id = d.pop("analysis_subject_id", UNSET)

        pipeline_finished = d.pop("pipeline_finished", UNSET)

        pipeline_failed = d.pop("pipeline_failed", UNSET)

        pipeline_progress = d.pop("pipeline_progress", UNSET)

        visible_to_user = d.pop("visible_to_user", UNSET)

        selected_variants_url = d.pop("selected_variants_url", UNSET)

        _analysis_info = d.pop("analysis_info", UNSET)
        analysis_info: Union[Unset, AnalysisDetailAnalysisInfo]
        if isinstance(_analysis_info, Unset):
            analysis_info = UNSET
        else:
            analysis_info = AnalysisDetailAnalysisInfo.from_dict(_analysis_info)

        _ethnicity = d.pop("ethnicity", UNSET)
        ethnicity: Union[Unset, AnalysisDetailEthnicity]
        if isinstance(_ethnicity, Unset):
            ethnicity = UNSET
        else:
            ethnicity = AnalysisDetailEthnicity(_ethnicity)

        annotation_databases = []
        _annotation_databases = d.pop("annotation_databases", UNSET)
        for annotation_databases_item_data in _annotation_databases or []:
            annotation_databases_item = AnalysisDetailAnnotationDatabasesItem.from_dict(annotation_databases_item_data)

            annotation_databases.append(annotation_databases_item)

        filter_sets = []
        _filter_sets = d.pop("filter_sets", UNSET)
        for filter_sets_item_data in _filter_sets or []:
            filter_sets_item = AnalysisDetailFilterSetsItem.from_dict(filter_sets_item_data)

            filter_sets.append(filter_sets_item)

        selected_variants = []
        _selected_variants = d.pop("selected_variants", UNSET)
        for selected_variants_item_data in _selected_variants or []:
            selected_variants_item = AnalysisDetailSelectedVariantsItem.from_dict(selected_variants_item_data)

            selected_variants.append(selected_variants_item)

        analysis_detail = cls(
            subject_id=subject_id,
            analysis_id=analysis_id,
            sample_id=sample_id,
            description=description,
            capture_kit=capture_kit,
            sequencer=sequencer,
            sample_type=sample_type,
            url=url,
            analysis_state=analysis_state,
            created_at=created_at,
            user_email=user_email,
            user_full_name=user_full_name,
            reference_genome=reference_genome,
            variants_to_keep=variants_to_keep,
            review_url=review_url,
            end_user_results_url=end_user_results_url,
            results_url=results_url,
            annotated_vcf_url=annotated_vcf_url,
            quality_control_report_url=quality_control_report_url,
            results_count=results_count,
            updated_at=updated_at,
            analysis_type=analysis_type,
            phenotypes=phenotypes,
            diseases=diseases,
            analysis_subject_id=analysis_subject_id,
            pipeline_finished=pipeline_finished,
            pipeline_failed=pipeline_failed,
            pipeline_progress=pipeline_progress,
            visible_to_user=visible_to_user,
            selected_variants_url=selected_variants_url,
            analysis_info=analysis_info,
            ethnicity=ethnicity,
            annotation_databases=annotation_databases,
            filter_sets=filter_sets,
            selected_variants=selected_variants,
        )

        analysis_detail.additional_properties = d
        return analysis_detail

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
