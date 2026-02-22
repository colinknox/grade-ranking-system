GRADES = ["F", "D", "C", "B", "A"]

class Grade:
    def __init__(self, letter):
        self.letter = letter
        self.grade_index = GRADES.index(self.letter)

    def get_numeric_value(self):
        return self.grade_index
    
    def is_better_than(self, other):
        if self.grade_index > other.grade_index:
            return True
        else:
            return False



b = Grade("B")
a = Grade("A")

# print(f"DEBUG: Numeric value = {a.get_numeric_value()}")
print(f"DEBUG: Is better than = {b.is_better_than(a)}")