from pathlib import Path

from services.file_service.upload_validation.schemas import ValidationResult


class UploadValidationService:
    def validate(self, file_name: str) -> ValidationResult:
        extension = Path(file_name).suffix.lower()
        if extension not in {".jpg", ".jpeg", ".png", ".gif", ".webp"}:
            raise ValueError(f"unsupported file extension: {extension}")
        return ValidationResult(is_valid=True)
