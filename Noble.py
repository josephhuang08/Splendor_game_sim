class Noble:
    def __init__(self, gem_requirement, points):
        self.gem_requirement = gem_requirement
        self.points = points

    def get_gem_requirement(self):
        return self.gem_requirement

    def get_points(self):
        return self.points