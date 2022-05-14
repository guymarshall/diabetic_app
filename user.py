class User:
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
    
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}', '{self.birthdate}')"