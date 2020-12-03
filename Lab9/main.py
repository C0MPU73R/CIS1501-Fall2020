class Assignment:

    def __init__(self):
        self._scores = []

    def add_score(self, score):
        self._scores.append(score)

    def get_max_score(self):
        return max(self._scores)

    def get_min_score(self):
        return min(self._scores)

    def get_average_score(self):
        return sum(self._scores) / len(self._scores)


class CurvedAssignment(Assignment):

    def get_max_score(self):
        return super().get_max_score() + self._get_adjustment()

    def get_min_score(self):
        return super().get_min_score() + self._get_adjustment()

    def get_average_score(self):
        return super().get_average_score() + self._get_adjustment()

    def _get_adjustment(self):
        return 100 - super().get_max_score()


first_assignment = CurvedAssignment()
first_assignment.add_score(70)
first_assignment.add_score(80)
first_assignment.add_score(90)

print("min: ", first_assignment.get_min_score())
print("average: ", first_assignment.get_average_score())
print("max: ", first_assignment.get_max_score())