GRADES = ["B", "B", "D", "A", "C"]

class Grade:
    def __init__(self, letter):
        self.letter = letter
        self.grade_index = GRADES.index(self.letter)

    def get_numeric_value(self):
        return self.grade_index



a = Grade("A")

print(f"DEBUG: Numeric value = {a.get_numeric_value()}")