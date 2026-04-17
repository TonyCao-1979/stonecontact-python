from domains.content.help_center.models import HelpCategory


class HelpCenterRepository:
    def list_categories(self) -> list[HelpCategory]:
        return [HelpCategory(id=1, name="Orders", is_enabled=True)]
