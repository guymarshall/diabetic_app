class Result:
    def __init__(self, user_id, time, date, blood_sugar, carbs, insulin_short, insulin_long, insulin_correction, notes):
        self.user_id = user_id
        self.time = time
        self.date = date
        self.blood_sugar = blood_sugar
        self.carbs = carbs
        self.insulin_short = insulin_short
        self.insulin_long = insulin_long
        self.insulin_correction = insulin_correction
        self.notes = notes
    
    def get_all():
        return ''
    
    def get_one(result_id):
        return ''
    
    def insert(result_data):
        return '';