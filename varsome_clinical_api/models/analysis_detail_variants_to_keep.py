from enum import Enum


class AnalysisDetailVariantsToKeep(str, Enum):
    ALL = "all"
    PASS_ONLY = "pass_only"

    def __str__(self) -> str:
        return str(self.value)
