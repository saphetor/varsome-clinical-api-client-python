import datetime
from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.sample_file_upload_status import SampleFileUploadStatus
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="SampleFileUpload")


@attr.s(auto_attribs=True)
class SampleFileUpload:
    """ """

    sample_file_name: str
    file: File
    id: Union[Unset, str] = UNSET
    number_of_variants_in_vcf: Union[Unset, int] = UNSET
    number_of_reads: Union[Unset, int] = UNSET
    number_of_bases_in_reads: Union[Unset, int] = UNSET
    uploaded_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, SampleFileUploadStatus] = UNSET
    messages: Union[Unset, str] = UNSET
    is_usable: Union[Unset, bool] = UNSET
    user_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sample_file_name = self.sample_file_name
        file = self.file.to_tuple()

        id = self.id
        number_of_variants_in_vcf = self.number_of_variants_in_vcf
        number_of_reads = self.number_of_reads
        number_of_bases_in_reads = self.number_of_bases_in_reads
        uploaded_at: Union[Unset, str] = UNSET
        if not isinstance(self.uploaded_at, Unset):
            uploaded_at = self.uploaded_at.isoformat()

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        messages = self.messages
        is_usable = self.is_usable
        user_email = self.user_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sample_file_name": sample_file_name,
                "file": file,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if number_of_variants_in_vcf is not UNSET:
            field_dict["number_of_variants_in_vcf"] = number_of_variants_in_vcf
        if number_of_reads is not UNSET:
            field_dict["number_of_reads"] = number_of_reads
        if number_of_bases_in_reads is not UNSET:
            field_dict["number_of_bases_in_reads"] = number_of_bases_in_reads
        if uploaded_at is not UNSET:
            field_dict["uploaded_at"] = uploaded_at
        if status is not UNSET:
            field_dict["status"] = status
        if messages is not UNSET:
            field_dict["messages"] = messages
        if is_usable is not UNSET:
            field_dict["is_usable"] = is_usable
        if user_email is not UNSET:
            field_dict["user_email"] = user_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sample_file_name = d.pop("sample_file_name")

        file = File(payload=BytesIO(d.pop("file")))

        id = d.pop("id", UNSET)

        number_of_variants_in_vcf = d.pop("number_of_variants_in_vcf", UNSET)

        number_of_reads = d.pop("number_of_reads", UNSET)

        number_of_bases_in_reads = d.pop("number_of_bases_in_reads", UNSET)

        _uploaded_at = d.pop("uploaded_at", UNSET)
        uploaded_at: Union[Unset, datetime.datetime]
        if isinstance(_uploaded_at, Unset):
            uploaded_at = UNSET
        else:
            uploaded_at = isoparse(_uploaded_at)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SampleFileUploadStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SampleFileUploadStatus(_status)

        messages = d.pop("messages", UNSET)

        is_usable = d.pop("is_usable", UNSET)

        user_email = d.pop("user_email", UNSET)

        sample_file_upload = cls(
            sample_file_name=sample_file_name,
            file=file,
            id=id,
            number_of_variants_in_vcf=number_of_variants_in_vcf,
            number_of_reads=number_of_reads,
            number_of_bases_in_reads=number_of_bases_in_reads,
            uploaded_at=uploaded_at,
            status=status,
            messages=messages,
            is_usable=is_usable,
            user_email=user_email,
        )

        sample_file_upload.additional_properties = d
        return sample_file_upload

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
