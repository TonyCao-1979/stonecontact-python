from dataclasses import dataclass


@dataclass(slots=True)
class UploadRequestContext:
    scheme: str
    file_name: str
    business_module: str | None = None


@dataclass(slots=True)
class UploadResult:
    relative_path: str
    public_url: str | None = None
