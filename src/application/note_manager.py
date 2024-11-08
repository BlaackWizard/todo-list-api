from dataclasses import dataclass
from datetime import datetime

from src.domain.services.note_services import NoteServices

@dataclass
class NoteManager:
    note_service: NoteServices

    def create_note(self, title: str, description: str,
                    created_at: datetime, updated_at: datetime):
       return self.note_service.create_note(title, description, created_at, updated_at)

    def mark_as_completed(self, note_id: int):
        self.note_service.complete_note(note_id)

    def remove_task(self, note_id: int):
        self.note_service.delete_note(note_id)