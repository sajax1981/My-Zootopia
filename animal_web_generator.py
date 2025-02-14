import json

def load_data(file_path):
    """
    Loads data from a JSON file
    Returns:
        JSON data as a dictionary for python
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
    Serialize a single animal into html format
    """
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<p class="card__text">\n'
    output += '<ul class="card__details">\n'

    if "diet" in animal_obj["characteristics"]:
        output += f'<li class="card__detail"><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n'

    if "locations" in animal_obj:
        output += f'<li class="card__detail"><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'

    if "type" in animal_obj["characteristics"]:
        output += f'<li class="card__detail"><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n'

    output += '</ul>\n'
    output += '</div>\n'
    output += '</li>\n'
    return output


def generate_html(data):
    """
    Generate html content for all animals
    """
    output = '<ul class="cards">\n'  # Start the unordered list

    for animal_obj in data:
            output += serialize_animal(animal_obj)

    output += '</ul>\n'  # Close the unordered list
    return output



#Load animal data from the JSON file
animals_data = load_data('animals_data.json')

final_output = generate_html(animals_data)

with open("animals_template.html", "r") as file:
    template_content = file.read()

# Replace with the generated animals.html
final_content = template_content.replace("__REPLACE_ANIMALS_INFO__", final_output)

print("Final HTML content:")
print(final_content)

with open("animals.html", "w") as file:
    file.write(final_content)

print("HTML file generated successfully: animals.html")
