import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

output = ''
for animal in animals_data:
    output += f"Name: {animal['name']}\n"

    if "diet" in animal["characteristics"]:
        output += f"Diet: {animal['characteristics']['diet']}\n"

    if "locations" in animal:
        output += f"Location: {animal['locations'][0]}\n"

    if "type" in animal["characteristics"]:
        output += f"Type: {animal['characteristics']['type']}\n"

    output += "\n"  # Add a new line between animals

# Read the template HTML content
with open("animals_template.html", "r") as file:
    template_content = file.read()

# Step 4: Replace the placeholder with the generated string
final_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 5: Write the new HTML content to a new file
with open("animals.html", "w") as file:
    file.write(final_content)

print("HTML file generated successfully: animals.html")
