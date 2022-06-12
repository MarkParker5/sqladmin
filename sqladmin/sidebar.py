from dataclasses import dataclass

@dataclass
class SidebarLink:
    text: str
    url: str
    new_blank: bool
