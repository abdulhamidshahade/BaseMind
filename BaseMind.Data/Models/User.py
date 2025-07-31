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