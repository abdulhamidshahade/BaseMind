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
    
    @classmethod
    def from_dictionary(cls, data: Dict[str, Any]) -> 'User':
        return cls(
            user_id=int(data['user_id']),
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            username=data.get('username', ''),
            is_bot=data.get('is_bot', False),
            language_code=data.get('language_code', 'en'),
            join_date=datetime.strptime(data.get('join_date', datetime.now().strftime('%Y-%m-%d %H:%M:%S')), '%Y-%m-%d %H:%M:%S'),
            last_activity=datetime.strptime(data.get('last_activity', datetime.now().strftime('%Y-%m-%d %H:%M:%S')), '%Y-%m-%d %H:%M:%S'),
            message_count=data.get('message_count', 0)
        )