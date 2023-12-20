import json

# Load the provided JSON file
file_path = '/mnt/data/102490243.json'

with open(file_path, 'r') as file:
    json_data = json.load(file)

# Function to extract properties from JSON data
def extract_properties(data, properties):
    def get_nested_property(data, path):
        try:
            for key in path.split('/'):
                data = data[key] if key != '*' else data[0]
            return data
        except (KeyError, IndexError, TypeError):
            return None

    extracted_data = {}
    for prop, data_type in properties.items():
        value = get_nested_property(data, prop)
        if data_type == 'int' and value is not None:
            value = int(value)
        extracted_data[prop] = value

    return extracted_data

# list of desired properties based on the corrected paths
desired_properties = {
    "data/name": "str",
    "data/gender": "str",
    "data/faith": "str",
    "data/age": "int",
    "data/hair": "str",
    "data/eyes": "str",
    "data/skin": "str",
    "data/height": "str",
    "data/weight": "str",
    "data/background/definition/shortDescription": "str",
    "data/background/customBackground/shortDescription": "str",
    "data/race/fullName": "str",
    "data/race/description": "str",
    "data/notes": "dict",
    "data/traits": "dict",
    "data/classes/*/definition/name": "str",
    "data/classes/*/subclassDefinition/name": "str"
}

# Extract the data
extracted_data = extract_properties(json_data, desired_properties)

extracted_data
