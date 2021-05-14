from enum import Enum


class AnalysisDetailEthnicity(str, Enum):
    VALUE_0 = ""
    AFR = "AFR"
    AMR = "AMR"
    ASJ = "ASJ"
    EAS = "EAS"
    FIN = "FIN"
    NFE = "NFE"
    SAS = "SAS"
    OTH = "OTH"

    def __str__(self) -> str:
        return str(self.value)
