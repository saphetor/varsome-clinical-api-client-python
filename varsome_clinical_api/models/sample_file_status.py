from enum import IntEnum


class SampleFileStatus(IntEnum):
    VALUE_0 = 0
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_1 = 1

    def __str__(self) -> str:
        return str(self.value)
