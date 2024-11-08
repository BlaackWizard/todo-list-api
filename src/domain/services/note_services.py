from dataclasses import dataclass
from datetime import datetime

from src.domain.repository.note_repository import BaseNoteRepository
from src.entities.note import NoteEntity


@dataclass
class NoteServices:
    note_repository: BaseNoteRepository

    def create_note(self, title: str, description: str, created_at: datetime,
                    updated_at: datetime):
        note = NoteEntity(id=None, title=title, description=description, created_at=created_at,
                          updated_at=updated_at)

        self.note_repository.save_note(note)
        return note

    def complete_note(self, note_id: int):
        note = self.note_repository.get_note_by_id(note_id)
        note.mark_completed()
        self.note_repository.save_note(note)

    def delete_note(self, note_id: int):
        note = self.note_repository.get_note_by_id(note_id)
        self.note_repository.delete_note(note)

