from dataclasses import dataclass


@dataclass(slots=True)
class ValidationRule:
    allowed_extensions: tuple[str, ...]
