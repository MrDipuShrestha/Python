travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]


def add_new_country(country_name, number_visit, city_names):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = number_visit
    new_country["cities"] = city_names
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint"])
print(travel_log)
