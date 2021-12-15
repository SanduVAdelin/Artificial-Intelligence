from Country import Country


class Map:
    def __init__(self, counties, constraints):
        self.countries = counties
        self.constraints = constraints

    def get_constraints(self):
        for constraint in self.constraints:
            print(f'{constraint[0].get_name()} , {constraint[1].get_name()}')

    def get_number_of_countries(self):
        return len(self.countries)