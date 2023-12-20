# Character Descriptions

This file includes multiple ways that the Arcane Paintbrush bot can get data to
be used for character art creation. This file only inlcudes ways that
characters may be described, not the different art styles to be used.

## DnDBeyond Characters

DnDBeyond is an online service that allows players of the game Dungeons & Dragons
to create and customize their characters for that role-playing game.

### DnDBeyond Character API

If given a DnD Beyond Character ID, which is in the form of a 9 digit integer,
the character details can be found by appending that Character ID to the
following base URL

https://character-service.dndbeyond.com/character/v3/character/

If the response to this API is "Unauthorized Access Attempt" the reason is most
likely that the Character Privacy option in the DnDBeyond Character Builder
hasn't been set to Public. Unless the character sheet is shared publicly the
Arcane Paintbrush app will not be able to access the character data.

### DnDBeyond Character JSON

If the attempt to use the API fails, the bot will then check to see if there is
a JSON file saved with the Character ID as the filename. If the file exists,
the bot will use this file as data about the character.

## Named Characters

This file contains names and descriptions of specific characters so that the
Arcane Paintbrush bot can represent these characters in a consistent manner. If
a DnDBeyond link is provided for that character, as well as a description in
this file, then use both description and DnDBeyond data to build up the correct
look.

### Aelar Fernblade

Aelar Fernblade is a female Wood Elf with an athletic build, tanned brown skin,
brown hair in a long braid and green eyes. She looks like she wears dark eye
shadow and has dark lips. She usually has a serious expression with a piercing
gaze.

Aelar is a Gloomstalker Ranger. She wears a hooded green cloak, brown leather
armour with two elven swords strapped to her back. She wears snake-skin
knee-length boots over leather trousers. Buckles and clasps on her clothing are
fashioned to resemble animal parts such as paws or teeth.

### Gimble Skip Hopper

* Character ID: 102490243

### Olwynne Callestra

Lady Olwynne Callestra is a female High Elf with a petite build, ethereal
grace, flawless fair skin, blonde hair in an elegant up-do style and blue eyes.
She is a wealthy noblewoman, and usually has a haughty expression.

She is a Bladesinger; she wears expensive silvery clothing such as kimonos and
heavily embroidered robes which are layered and often decorated with subtle
leaf or moon motifs. Her clothes show off her elegant figure.

When moving and fighting she appears to be dancing and the very air seems to
swirl around her while magical energy crackles in the air.

### Lady Eleanor Saldana

Lady Eleanor Saldana is a High Elf Druid, the daughter of the King and Queen of
the village deep in the forest where she grew up. She has pale green eyes, a
tall and elegant figure with long strawberry blonde hair, which she wears
loosely with wild flowers and twigs keeping it in order.

She likes to dress in sensible warm clothing made from strong fabrics adorned
and embellished with natural decorations such as flowers, sprigs, etc. She is
often found casting spells to benefit the woodland animals she shepherds.

Tiring of life in the village she set out into the world as an adventurer. She
loves the forest and all the forest creatures. She often befriends these
animals, even large ones such as wild boar and wolves. She fights to ensure
that the wild places of the world remain unspoilt by urbanisation. She
especially hates loggers who cut down forests uncaringly for profit.

### Pali

#### Stardust

Stardust is a Palomino coloured Arabian mare with silver white mane and tail
which are left loose. Stardust has a dark sooty nose and a diamond on her
forehead. She is normally seen cantering around her paddock.
