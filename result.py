from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Result:
    user_id: int
    time: time
    date: date
    blood_sugar: float
    carbs: int
    insulin_short: int
    insulin_long: int
    insulin_correction: int
    notes: str
    
    def get_all():
        return ''
    
    def get_one(result_id):
        return ''
    
    def insert(result_data):
        return ''