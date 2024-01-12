country = input("Add a country you have visited\n") # Add country name
visits = int(input(f"How many times have you visited {country}\n")) # Number of visits
list_of_cities = str(input(f"Which cities have you visited in {country}\n")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    cities_list = []
    new_country["country"] = name
    new_country["visits"] = times_visited
    cities_list.append(cities_visited)
    new_country["cities"] = cities_list
    travel_log.append(new_country)






add_new_country(name=country, times_visited=visits, cities_visited=list_of_cities)
print(travel_log)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")