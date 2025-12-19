import json
from dataclasses import dataclass, asdict
from typing import List, Self

@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def est_classique(self) -> bool:
        """Returns True if the film was released before the year 2000."""
        return self.annee < 2000

    def to_json(self) -> str:
        """Converts the Film instance to a JSON string."""
        return json.dumps(asdict(self), ensure_ascii=False)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Creates a Film instance from a JSON string."""
        data = json.loads(json_str)
        return cls(**data)

    def __lt__(self, other: Self) -> bool:
        """Defines natural ordering based on the rating (note) ascending."""
        if not isinstance(other, Film):
            return NotImplemented
        return self.note < other.note

# --- Extension: Favorites List Management ---

def favoris_to_json(films: List[Film]) -> str:
    """Serializes a list of Film objects to a JSON array."""
    return json.dumps([asdict(f) for f in films], ensure_ascii=False)

def favoris_from_json(json_str: str) -> List[Film]:
    """Deserializes a JSON array into a list of Film objects."""
    data_list = json.loads(json_str)
    return [Film(**data) for data in data_list]
