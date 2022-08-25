destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", 
"Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

desind = get_destination_index("Paris, France")
print(desind)

test_destination_index = get_traveler_location(test_traveler)
print(str(test_destination_index))