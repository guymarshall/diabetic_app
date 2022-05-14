class Employee:
    """A sample Employee class"""

    def __init__(self, last, first, pay):#last and first the wrong way around
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"