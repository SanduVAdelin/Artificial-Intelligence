class Country:
    def __init__(self, name, available_colors):
        self.name = name
        self.available_colors = available_colors

    def get_available_colors(self):
        list_of_available_colors = []
        for available_color in self.available_colors:
            list_of_available_colors.append(available_color)
        return list_of_available_colors

    def update_available_color(self, constraints):
        for constraint in constraints:
            if self.name == constraint[0].get_name():
                print(f'Tara vecina este : {constraint[1].get_name()}')
                print('Culorile vecinului sunt : ')
                constraint[1].get_available_colors()
            if self.name == constraint[1].get_name():
                print(f'Tara vecina este : {constraint[0].get_name()}')
                print('Culorile vecinului sunt : ')
                constraint[0].get_available_colors()

    def get_name(self):
        return self.name
