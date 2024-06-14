class Student:

    def __init__(self, id, name, mark):
        self.Id = id
        self.Name = name
        self.Mark = mark

    def __repr__(self):
        return f"{self.Id}, {self.Name}, {self.Mark}"