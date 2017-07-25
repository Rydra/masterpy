import itertools
class Result:
    def __init__(self, black, white):
        self.black = black
        self.white = white

class Validator:

    def _to_dictionary(self, combination):
        return dict((k, list(g)) for k, g in itertools.groupby(combination, lambda color: color))

    def validate(self, solution, combination):
        black = len(list(filter(lambda xy: xy[0] == xy[1], zip(solution, combination))))

        grouped_by_color_solution = self._to_dictionary(solution)
        grouped_by_color_combination = self._to_dictionary(combination)

        white = 0
        commoncolors = set(grouped_by_color_solution.keys()).intersection(set(grouped_by_color_combination.keys()))
        for color in commoncolors:
            white += min(len(grouped_by_color_solution[color]), len(grouped_by_color_combination[color]))

        return Result(black, white - black)
