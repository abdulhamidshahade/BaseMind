from dataclasses import dataclass, field
from typing import Dict, Any
from datetime import datetime

@dataclass
class User:
    user_id: int
    first_name: str
    last_name: str = ""
    username: str = ""
    is_bot: bool = False
    language_code: str = "tr"
    join_date: datetime = field(default_factory=datetime.now)
    last_activity: datetime = field(default_factory=datetime.now)
    message_count: int = 0

    @classmethod
    def to_dictionary(self) -> Dict[str, Any]:
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'is_bot': self.is_bot,
            'language_code': self.language_code,
            'join_date': self.join_date,
            'last_activity': self.last_activity,
            'message_count': self.message_count
        }