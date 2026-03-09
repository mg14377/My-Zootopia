import json


# JSON-Datei laden und Daten als Python-Objekt zurückgeben
def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


# Einzelnes Tierobjekt in HTML-Code umwandeln
def serialize_animal(animal):
    output = ''

    # Start der HTML-Karte für ein Tier
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal["name"]}</div>\n'
    output += '<p class="card__text">\n'

    # Ernährung ausgeben, falls vorhanden
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f'<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

    # Ersten Standort aus der Liste ausgeben
    if "locations" in animal:
        output += f'<strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    # Tier-Typ ausgeben, falls vorhanden
    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f'<strong>Type:</strong> {animal["characteristics"]["type"].capitalize()}<br/>\n'

    # Ende der HTML-Karte
    output += '</p>\n'
    output += '</li>\n'

    return output


# Tierdaten aus der JSON-Datei laden
animals_data = load_data("animals_data.json")


# HTML-Vorlage einlesen
with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()


# HTML-Code für alle Tiere erzeugen
output = ""

for animal in animals_data:
    output += serialize_animal(animal)


# Platzhalter in der HTML-Vorlage durch generierte Tierkarten ersetzen
html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)


# Fertige HTML-Seite in eine neue Datei schreiben
with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_output)