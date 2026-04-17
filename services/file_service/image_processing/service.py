from services.file_service.image_processing.schemas import ImageProcessRequest, ImageProcessResponse


class ImageProcessingService:
    def process(self, request: ImageProcessRequest) -> ImageProcessResponse:
        return ImageProcessResponse(rule=request.rule, variants=[])
