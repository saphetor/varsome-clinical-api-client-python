from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.multi_sample_analysis_from_vcf_files_components_item import MultiSampleAnalysisFromVCFFilesComponentsItem
from ..models.multi_sample_analysis_from_vcf_files_gene_list_analysis_based_on_phenotypes import (
    MultiSampleAnalysisFromVCFFilesGeneListAnalysisBasedOnPhenotypes,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiSampleAnalysisFromVCFFiles")


@attr.s(auto_attribs=True)
class MultiSampleAnalysisFromVCFFiles:
    """ """

    components: List[MultiSampleAnalysisFromVCFFilesComponentsItem]
    tags: Union[Unset, List[str]] = UNSET
    gene_list_analysis_based_on_phenotypes: Union[
        Unset, MultiSampleAnalysisFromVCFFilesGeneListAnalysisBasedOnPhenotypes
    ] = UNSET
    genes: Union[Unset, List[str]] = UNSET
    varsome_gene_list_id: Union[Unset, str] = UNSET
    panelapp_gene_list_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()

            components.append(components_item)

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        gene_list_analysis_based_on_phenotypes: Union[Unset, str] = UNSET
        if not isinstance(self.gene_list_analysis_based_on_phenotypes, Unset):
            gene_list_analysis_based_on_phenotypes = self.gene_list_analysis_based_on_phenotypes.value

        genes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.genes, Unset):
            genes = self.genes

        varsome_gene_list_id = self.varsome_gene_list_id
        panelapp_gene_list_id = self.panelapp_gene_list_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "components": components,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if gene_list_analysis_based_on_phenotypes is not UNSET:
            field_dict["gene_list_analysis_based_on_phenotypes"] = gene_list_analysis_based_on_phenotypes
        if genes is not UNSET:
            field_dict["genes"] = genes
        if varsome_gene_list_id is not UNSET:
            field_dict["varsome_gene_list_id"] = varsome_gene_list_id
        if panelapp_gene_list_id is not UNSET:
            field_dict["panelapp_gene_list_id"] = panelapp_gene_list_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = MultiSampleAnalysisFromVCFFilesComponentsItem.from_dict(components_item_data)

            components.append(components_item)

        tags = cast(List[str], d.pop("tags", UNSET))

        _gene_list_analysis_based_on_phenotypes = d.pop("gene_list_analysis_based_on_phenotypes", UNSET)
        gene_list_analysis_based_on_phenotypes: Union[
            Unset, MultiSampleAnalysisFromVCFFilesGeneListAnalysisBasedOnPhenotypes
        ]
        if isinstance(_gene_list_analysis_based_on_phenotypes, Unset):
            gene_list_analysis_based_on_phenotypes = UNSET
        else:
            gene_list_analysis_based_on_phenotypes = MultiSampleAnalysisFromVCFFilesGeneListAnalysisBasedOnPhenotypes(
                _gene_list_analysis_based_on_phenotypes
            )

        genes = cast(List[str], d.pop("genes", UNSET))

        varsome_gene_list_id = d.pop("varsome_gene_list_id", UNSET)

        panelapp_gene_list_id = d.pop("panelapp_gene_list_id", UNSET)

        multi_sample_analysis_from_vcf_files = cls(
            components=components,
            tags=tags,
            gene_list_analysis_based_on_phenotypes=gene_list_analysis_based_on_phenotypes,
            genes=genes,
            varsome_gene_list_id=varsome_gene_list_id,
            panelapp_gene_list_id=panelapp_gene_list_id,
        )

        multi_sample_analysis_from_vcf_files.additional_properties = d
        return multi_sample_analysis_from_vcf_files

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
