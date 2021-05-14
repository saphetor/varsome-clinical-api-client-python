from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.analysis_create_from_uploaded_vcf_files_ethnicity import AnalysisCreateFromUploadedVCFFilesEthnicity
from ..models.analysis_create_from_uploaded_vcf_files_gene_list_analysis_based_on_phenotypes import (
    AnalysisCreateFromUploadedVCFFilesGeneListAnalysisBasedOnPhenotypes,
)
from ..models.analysis_create_from_uploaded_vcf_files_reference_genome import (
    AnalysisCreateFromUploadedVCFFilesReferenceGenome,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisCreateFromUploadedVCFFiles")


@attr.s(auto_attribs=True)
class AnalysisCreateFromUploadedVCFFiles:
    """ """

    subject_id: str
    sample_file_ids: List[str]
    description: Union[Unset, str] = UNSET
    capture_kit_id: Union[Unset, int] = UNSET
    reference_genome: Union[
        Unset, AnalysisCreateFromUploadedVCFFilesReferenceGenome
    ] = AnalysisCreateFromUploadedVCFFilesReferenceGenome.HG19
    phenotype_ids: Union[Unset, List[str]] = UNSET
    disease_ids: Union[Unset, List[str]] = UNSET
    ethnicity: Union[Unset, AnalysisCreateFromUploadedVCFFilesEthnicity] = UNSET
    sequencer: Union[Unset, str] = UNSET
    gene_list_analysis_based_on_phenotypes: Union[
        Unset, AnalysisCreateFromUploadedVCFFilesGeneListAnalysisBasedOnPhenotypes
    ] = UNSET
    genes: Union[Unset, List[str]] = UNSET
    varsome_gene_list_id: Union[Unset, str] = UNSET
    panelapp_gene_list_id: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
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
        gene_list_analysis_based_on_phenotypes: Union[Unset, str] = UNSET
        if not isinstance(self.gene_list_analysis_based_on_phenotypes, Unset):
            gene_list_analysis_based_on_phenotypes = self.gene_list_analysis_based_on_phenotypes.value

        genes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.genes, Unset):
            genes = self.genes

        varsome_gene_list_id = self.varsome_gene_list_id
        panelapp_gene_list_id = self.panelapp_gene_list_id
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

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
        if gene_list_analysis_based_on_phenotypes is not UNSET:
            field_dict["gene_list_analysis_based_on_phenotypes"] = gene_list_analysis_based_on_phenotypes
        if genes is not UNSET:
            field_dict["genes"] = genes
        if varsome_gene_list_id is not UNSET:
            field_dict["varsome_gene_list_id"] = varsome_gene_list_id
        if panelapp_gene_list_id is not UNSET:
            field_dict["panelapp_gene_list_id"] = panelapp_gene_list_id
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject_id = d.pop("subject_id")

        sample_file_ids = cast(List[str], d.pop("sample_file_ids"))

        description = d.pop("description", UNSET)

        capture_kit_id = d.pop("capture_kit_id", UNSET)

        _reference_genome = d.pop("reference_genome", UNSET)
        reference_genome: Union[Unset, AnalysisCreateFromUploadedVCFFilesReferenceGenome]
        if isinstance(_reference_genome, Unset):
            reference_genome = UNSET
        else:
            reference_genome = AnalysisCreateFromUploadedVCFFilesReferenceGenome(_reference_genome)

        phenotype_ids = cast(List[str], d.pop("phenotype_ids", UNSET))

        disease_ids = cast(List[str], d.pop("disease_ids", UNSET))

        _ethnicity = d.pop("ethnicity", UNSET)
        ethnicity: Union[Unset, AnalysisCreateFromUploadedVCFFilesEthnicity]
        if isinstance(_ethnicity, Unset):
            ethnicity = UNSET
        else:
            ethnicity = AnalysisCreateFromUploadedVCFFilesEthnicity(_ethnicity)

        sequencer = d.pop("sequencer", UNSET)

        _gene_list_analysis_based_on_phenotypes = d.pop("gene_list_analysis_based_on_phenotypes", UNSET)
        gene_list_analysis_based_on_phenotypes: Union[
            Unset, AnalysisCreateFromUploadedVCFFilesGeneListAnalysisBasedOnPhenotypes
        ]
        if isinstance(_gene_list_analysis_based_on_phenotypes, Unset):
            gene_list_analysis_based_on_phenotypes = UNSET
        else:
            gene_list_analysis_based_on_phenotypes = (
                AnalysisCreateFromUploadedVCFFilesGeneListAnalysisBasedOnPhenotypes(
                    _gene_list_analysis_based_on_phenotypes
                )
            )

        genes = cast(List[str], d.pop("genes", UNSET))

        varsome_gene_list_id = d.pop("varsome_gene_list_id", UNSET)

        panelapp_gene_list_id = d.pop("panelapp_gene_list_id", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        analysis_create_from_uploaded_vcf_files = cls(
            subject_id=subject_id,
            sample_file_ids=sample_file_ids,
            description=description,
            capture_kit_id=capture_kit_id,
            reference_genome=reference_genome,
            phenotype_ids=phenotype_ids,
            disease_ids=disease_ids,
            ethnicity=ethnicity,
            sequencer=sequencer,
            gene_list_analysis_based_on_phenotypes=gene_list_analysis_based_on_phenotypes,
            genes=genes,
            varsome_gene_list_id=varsome_gene_list_id,
            panelapp_gene_list_id=panelapp_gene_list_id,
            tags=tags,
        )

        analysis_create_from_uploaded_vcf_files.additional_properties = d
        return analysis_create_from_uploaded_vcf_files

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
