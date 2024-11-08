from typing import List

from src.infrastructure.note.models import Note
from src.domain.repository.note_repository import BaseNoteRepository
from src.entities.note import NoteEntity

class NoteRepositoryImpl(BaseNoteRepository):
    def get_note_by_id(self, id: int) -> NoteEntity:
        note = Note.objects.get(id=id)
        return self._convert_to_entity(note)

    def save_note(self, note: NoteEntity) -> None:
        note = self._convert_to_model(note)
        note.save()

    def delete_note(self, note: NoteEntity) -> None:
        note = self._convert_to_model(note)
        note.delete()

    def list_notes(self) -> List[NoteEntity]:
        notes = Note.objects.all()
        return [self._convert_to_entity(note) for note in notes]

    def _convert_to_entity(self, model):
         return NoteEntity(id=model.id, title=model.title, description=model.description,
                     created_at=model.created_at, updated_at=model.updated_at)

    def _convert_to_model(self, entity):
        return Note(id=entity.id, title=entity.title, description=entity.description,
                    created_at=entity.created_at, updated_at=entity.updated_at)