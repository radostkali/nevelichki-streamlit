from enum import StrEnum, auto


class Species(StrEnum):
    MOLE = auto()
    HARE = auto()
    CAT = auto()
    PARROT = auto()
    RAT = auto()
    BADGER = auto()
    ARCTIC_FOX = auto()
    PENGUIN = auto()


SPECIES_TO_NAME_MAP = {
    Species.MOLE: 'Крот',
    Species.HARE: 'Заяц',
    Species.CAT: 'Кот',
    Species.PARROT: 'Попугай',
    Species.RAT: 'Крыса',
    Species.BADGER: 'Барсук',
    Species.ARCTIC_FOX: 'Песец',
    Species.PENGUIN: 'Пингвин',
}
