from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class SearchedWord:
    """Class for searched terms"""
    word: str
    definition: str
    lang: str
    first_searched: datetime
    last_searched: datetime
    times_searched: int

    @classmethod
    def from_json(cls, data: dict) -> 'SearchedWord':
        return cls(
            word=data['word'],
            definition=data['definition'],
            lang=data['lang'],
            first_searched=datetime.fromisoformat(data['first_searched']),
            last_searched=datetime.fromisoformat(data['last_searched']),
            times_searched=data['times_searched']
        )

    def to_json(self) -> dict:
        return {
            **asdict(self),
            'first_searched': self.first_searched.isoformat(),
            'last_searched': self.last_searched.isoformat()
        }
