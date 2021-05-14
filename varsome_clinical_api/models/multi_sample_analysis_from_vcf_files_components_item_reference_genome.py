from enum import Enum


class MultiSampleAnalysisFromVCFFilesComponentsItemReferenceGenome(str, Enum):
    HG19 = "hg19"
    HG38 = "hg38"

    def __str__(self) -> str:
        return str(self.value)
