
cities = ["Vizag", "Guntur", "Vijayawada", "Kakinada", "Vizianagaram"]
print("Initial list of cities:", cities)


middle_index = len(cities) // 2
print( cities[middle_index])


subset_cities = cities[:3]
print( subset_cities)


sorted_cities = sorted(cities)
print( sorted_cities)


cities.append("Rajahmundry")
print( cities)


cities.pop(0)
print( cities)


def get_list_length(city_list):
    return len(city_list)


length = get_list_length(cities)
print("Length of the list:", length)
