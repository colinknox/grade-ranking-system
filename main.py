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

    def is_same_as(self, other):
        if self.grade_index == other.grade_index:
            return True
        else:
            return False