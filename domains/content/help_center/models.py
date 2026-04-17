from dataclasses import dataclass


@dataclass(slots=True)
class HelpCategory:
    id: int
    name: str
    is_enabled: bool


@dataclass(slots=True)
class HelpArticle:
    id: int
    title: str
    content: str
