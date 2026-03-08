import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

output = ""

for animal in animals_data:
    output += f"Name: {animal['name']}\n"

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"Diet: {animal['characteristics']['diet']}\n"

    if "locations" in animal:
        output += f"Location: {animal['locations'][0]}\n"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"Type: {animal['characteristics']['type']}\n"

    output += "\n"

html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_output)

for animal in animals_data:              # Iteriert durch alle Tiere in der Liste

    print("Name:", animal["name"])

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        print("Diet:", animal["characteristics"]["diet"])

    if "locations" in animal:
        print("Location:", animal["locations"][0])

    if "characteristics" in animal and "type" in animal["characteristics"]:
        print("Type:", animal["characteristics"]["type"])

    print()