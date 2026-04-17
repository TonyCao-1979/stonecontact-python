from dataclasses import dataclass


@dataclass(slots=True)
class ImageVariant:
    variant_name: str
    relative_path: str
