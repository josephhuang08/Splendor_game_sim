class Card:
    def __init__(self, level, gem_type, cost, points):
        self.level = level
        self.gem_type = gem_type
        self.cost = cost
        self.points = points

    def get_level(self):
        return self.level

    def get_gem_type(self):
        return self.gem_type

    def get_cost(self):
        return self.cost

    def get_points(self):
        return self.points