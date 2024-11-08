from dataclasses import dataclass
from datetime import datetime


@dataclass
class NoteEntity:
    id: int
    title: str
    description: str
    completed = False
    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        ...

    def mark_completed(self):
        self.completed = True
