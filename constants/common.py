from enum import StrEnum, auto


STATE_KEY_CHARACTER = 'character'


class PagesPath(StrEnum):
    HELLO = 'app.py'
    SPECIES_SELECT = 'pages/species_select_page.py'
    CLASS_SELECT = 'pages/class_select_page.py'


class CharacterCreatingStage(StrEnum):

    SPECIES_SELECT = auto()
    CLASS_SELECT = auto()
