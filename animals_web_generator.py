import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:              # Iteriert durch alle Tiere in der Liste

    print("Name:", animal["name"])

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        print("Diet:", animal["characteristics"]["diet"])

    if "locations" in animal:
        print("Location:", animal["locations"][0])

    if "characteristics" in animal and "type" in animal["characteristics"]:
        print("Type:", animal["characteristics"]["type"])

    print()