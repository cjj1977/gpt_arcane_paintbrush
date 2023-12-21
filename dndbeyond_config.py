# A dictionary of properties we want to extract from the D&D Beyond API. The
# keys are the paths to the properties we want to extract. The values are the
# data types we want to convert the values to. We use a path-like syntax to
# specify nested properties. For example, "data/name" will extract the "name"
# property from the "data" object. "data/classes/*/definition/name" will
# extract the "name" property from the "definition" object of each item in the
# "classes" array. We can use "*" to specify that we want to extract the
# property from each item in an array.
#
CHARACTER_PROPERTIES = {
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
    "data/classes/*/subclassDefinition/name": "str",
}

# The base URL for the D&D Beyond API
DDB_BASE_URL = "https://character-service.dndbeyond.com/character/v3/character/"
