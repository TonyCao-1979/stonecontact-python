from pydantic import BaseModel


class ImageProcessRequest(BaseModel):
    relative_path: str
    rule: str


class ImageVariantItem(BaseModel):
    variant_name: str
    relative_path: str


class ImageProcessResponse(BaseModel):
    rule: str
    variants: list[ImageVariantItem]
