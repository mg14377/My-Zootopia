import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal["name"]}</div>\n'
    output += '<p class="card__text">\n'

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f'<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

    if "locations" in animal:
        output += f'<strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f'<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

    output += '</p>\n'
    output += '</li>\n'

    return output


animals_data = load_data('animals_data.json')

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

output = ""

for animal in animals_data:
    output += serialize_animal(animal)

html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_output)