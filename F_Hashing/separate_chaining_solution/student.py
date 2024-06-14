class Student:
    def __init__(self, name, age, mark):
        self.Name = name
        self.Age = age
        self.Mark = mark

    def __repr__(self):
        return f"{self.Name}, {self.Age}, {self.Mark}"