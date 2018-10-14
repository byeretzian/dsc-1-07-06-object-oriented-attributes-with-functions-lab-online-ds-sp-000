class School():
    def __init__(self, name = None, roster = {}):
        self.name = name
        self.roster = roster
    def add_student(self, name, grade):
        if grade not in self.roster.keys():
            self.roster[grade] = []
            self.roster[grade].append(name)
        else:
            self.roster[grade].append(name)
    def grade(self, grade):
        return self.roster.get(grade)
    def sort_roster():
        for grade in self.roster:
            self.roster[grade] = sorted(self.roster.get(grade))
            return self.roster
