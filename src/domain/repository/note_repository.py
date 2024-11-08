from typing import List
from abc import ABC, abstractmethod
from src.entities.note import NoteEntity


class BaseNoteRepository(ABC):
    @abstractmethod
    def get_note_by_id(self, id: int) -> NoteEntity:
        ...
    @abstractmethod
    def save_note(self, note: NoteEntity) -> None:
        ...
    @abstractmethod
    def delete_note(self, note: NoteEntity) -> None:
        ...
    @abstractmethod
    def list_notes(self) -> List[NoteEntity]:
        ...

