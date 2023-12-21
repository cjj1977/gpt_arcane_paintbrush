import json
import requests

# local imports
from dndbeyond_config import CHARACTER_PROPERTIES, DDB_BASE_URL


def get_character_ids(path: str = "./characters/characters.md") -> iter:
    """
    An iterable function that yields character IDs from the characters.md file.

    We read the contents of the characters.md file and extract character IDs.
    These will be in the form "* Character ID: <id>". We want to extract the ID
    yield the IDs as we discover them.

    :param path: The path to the characters.md file
    :return: An iterable of character IDs
    """
    with open(path, "r") as file:
        file_contents = file.read()

    # Split the file contents into lines
    lines = file_contents.split("\n")

    # Extract the character IDs
    for line in lines:
        if line.startswith("* Character ID:"):
            yield line.split(": ")[1]


def _extract_properties(data: dict, properties: dict) -> dict:
    """
    Function to extract specific properties from JSON data.

    We take a dictionary of properties and data types and extract the
    corresponding values from the JSON data. We return a dictionary of the
    extracted properties.

    :param data: The JSON data to extract properties from
    :param properties: A dictionary of properties and data types
    :return: A dictionary of extracted properties
    """

    def _get_nested_property(data, path):
        try:
            for key in path.split("/"):
                data = data[key] if key != "*" else data[0]
            return data
        except (KeyError, IndexError, TypeError):
            return None

    extracted_data = {}
    for prop, data_type in properties.items():
        value = _get_nested_property(data, prop)
        if data_type == "int" and value is not None:
            value = int(value)
        extracted_data[prop] = value

    return extracted_data


def get_dndbeyond_data(character_id: str) -> dict:
    """
    Function to get character data from D&D Beyond API. We append the character
    ID to the base URL and make a GET request to the resulting URL. We then
    filter the JSON response using extract_properties() and return the result.
    """
    url = f"{DDB_BASE_URL}{character_id}"
    response = requests.get(url)
    data = response.json()
    return _extract_properties(data, CHARACTER_PROPERTIES)


def save_character(character_id, data):
    """
    Function to save character data to a JSON file
    """
    with open(f"./characters/{character_id}.json", "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    for character_id in get_character_ids():
        print(f"Getting character {character_id}...")
        data = get_dndbeyond_data(character_id)
        save_character(character_id, data)
