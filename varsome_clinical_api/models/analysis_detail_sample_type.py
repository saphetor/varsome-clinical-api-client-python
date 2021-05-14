from enum import Enum


class AnalysisDetailSampleType(str, Enum):
    GERMLINE = "germline"
    TUMOUR = "tumour"

    def __str__(self) -> str:
        return str(self.value)
