from dataclasses import dataclass


@dataclass(slots=True)
class StoredFile:
    relative_path: str
    content_type: str | None = None
    size: int | None = None
