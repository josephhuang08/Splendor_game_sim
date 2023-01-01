import csv
import random

class Noble:
    def __init__(self, gem_requirement, points):
        self.gem_requirement = gem_requirement
        self.points = points

    def get_gem_requirement(self):
        return self.gem_requirement

    def get_points(self):
        return self.points

class NobleList:
    def __init__(self):
        self.all = []
        # noblelist.csv holds the info for nobles
        with open('data/noblelist.csv', 'r') as file:
            # Create a reader object and skip the first row of csv file
            reader = csv.reader(file, delimiter=';')
            next(reader) 
            # Iterate through the rows of the file. Each row contains [points;green;red;blue;white;black]
            for row in reader:
                # convert the list of gem requirements into int
                temp = [row[1], row[2], row[3], row[4], row[5]]
                req = [int(x) if x else 0 for x in temp]
                # Create a Noble object and set its attributes
                new_Noble = Noble(req, row[0])
                self.all.append(new_Noble)

    # gets the number of nobles needed
    def new_nobles(self, num):
        return random.sample(self.all, num)

'''
    def print_list(self):
        temp = self.new_nobles(3)
        for i, noble in enumerate(temp):
            print("noble no.", i)
            print("requierements: ", noble.get_gem_requirement())
            print("points: ", noble.get_points())
            print()

list = NobleList()
list.print_list()
'''