from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class User:
    user_id: int
    first_name: str
    last_name: str
    sex: str

    def get_all():
        return ''
    
    def get_one(user_id):
        return ''
    
    def insert(user_id):
        return '';
