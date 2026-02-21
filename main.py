GRADES = ["B", "B", "D", "A", "C"]

class Grade:
    def __init__(self, letter):
        self.letter = letter
        self.grade_index = GRADES.index(self.letter)



a = Grade("A")