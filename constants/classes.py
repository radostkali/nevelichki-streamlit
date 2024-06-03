from enum import StrEnum, auto


class Class(StrEnum):
    INVENTOR = auto()
    WARRIOR = auto()
    RASCAL = auto()
    AFFECTOR = auto()
    BARBARIAN = auto()


SPECIES_TO_NAME_MAP = {
    Class.INVENTOR: 'Изобретатель',
    Class.WARRIOR: 'Воин',
    Class.RASCAL: 'Плут',
    Class.AFFECTOR: 'Аффектор',
    Class.BARBARIAN: 'Варвар',
}
