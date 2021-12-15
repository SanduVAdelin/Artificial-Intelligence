import random

from Map import Map
from Country import Country


def select_value_FC(domains: list, country_index, constraints):
    while domains[country_index]:
        a = random.choice(domains[country_index])
        # print(a)
        domains[country_index].remove(a)
        empty_domain = False
        for k in range(country_index + 1, len(domains)):
            for b in domains[k]:
                # print(b)
                if a == b:
                    for pair in constraints:
                        if pair[0].get_name() == countries[country_index].get_name() and pair[1].get_name() == \
                                countries[k].get_name():
                            domains[k].remove(b)
            if len(domains[k]) == 0:
                empty_domain = True
        if empty_domain:
            for k in range(country_index + 1, len(domains)):
                domains[k].append(a)
        else:
            return a
    domains[country_index].append(a)
    return


def minimum_remaining_values(domains):
    min = 3
    index = 0
    for domain in domains:
        if len(domain) < min:
            min = len(domain)
            index = domains.index(domain)
    return index


if __name__ == '__main__':

    WA = Country('WA', ['red', 'green', 'blue'])
    SA = Country('SA', ['red', 'green'])
    NT = Country('NT', ['green'])

    x = int(input('''Utilizam MRV pentru algoritmul de Forward Checking 
    1. DA
    2. NU \n'''))

    countries = [WA, SA, NT]
    constraints = [(WA, SA), (WA, NT), (SA, WA), (SA, NT), (NT, WA), (NT, SA)]
    main_map = Map(countries, constraints)

    # copiem toate domeniile
    wa_domain = WA.get_available_colors()
    sa_domain = SA.get_available_colors()
    nt_domain = NT.get_available_colors()
    domains = [wa_domain, sa_domain, nt_domain]

    if x == 1:
        sorted_countries = sorted(countries, key=lambda country: len(country.get_available_colors()))
        sorted_domains = sorted(domains, key=lambda x : len(x))

    # T = Country('T', ['red', 'blue', 'green'])
    # WA = Country('WA', ['red'])
    # NT = Country('NT', ['red', 'blue', 'green'])
    # SA = Country('SA', ['red', 'blue', 'green'])
    # Q = Country('Q', ['green'])
    # NSW = Country('NSW', ['red', 'blue', 'green'])
    # V = Country('V', ['red', 'blue', 'green'])
    #
    # countries = [T, WA, NT, SA, Q, NSW, V]
    #
    # constraints = [(T, V), (WA, NT), (WA, SA), (NT, WA), (NT, Q), (NT, SA), (SA, WA), (SA, NT), (SA, Q), (SA, NSW),
    #                (SA, V), (Q, NT), (Q, SA), (Q, NSW), (NSW, Q), (NSW, SA), (NSW, V), (V, SA), (V, NSW), (V, T)]
    #
    # main_map = Map(countries, constraints)
    #
    # wa_domain = WA.get_available_colors()
    # sa_domain = SA.get_available_colors()
    # nt_domain = NT.get_available_colors()
    # t_domain = T.get_available_colors()
    # q_domain = Q.get_available_colors()
    # nsw_domain = NSW.get_available_colors()
    # v_domain = V.get_available_colors()
    #
    # domains = [t_domain, wa_domain, nt_domain, sa_domain, q_domain, nsw_domain, v_domain]

    solution = []
    if x == 1:
        countries = sorted_countries
        domains = sorted_domains

    i = 0
    while i < main_map.get_number_of_countries():
        current_country = countries[i]
        # solution.append(select_value_FC(domains, i, constraints))
        current_color = select_value_FC(domains, i, constraints)
        if current_color is None:
            i = i - 1
            choose_color = solution[i]
            solution.remove(choose_color)
            for k in range(i + 1, len(domains)):
                if choose_color in countries[k].get_available_colors():
                    domains[k].append(choose_color)
        else:
            i = i + 1
            solution.append(current_color)

    if i == 0:
        print('Inconsistent')
    else:
        for i in range(0, len(solution)):
            print(f'{countries[i].get_name()} are culoarea : {solution[i]}')
