from enum import StrEnum, auto


class Ability(StrEnum):
    STRENGTH = auto()
    DEXTERITY = auto()
    CONSTITUTION = auto()
    INTELLIGENCE = auto()
    WISDOM = auto()
    CHARISMA = auto()


ABILITIES_TO_NAME_MAP = {
    Ability.STRENGTH: 'Сила',
    Ability.DEXTERITY: 'Ловкость',
    Ability.CONSTITUTION: 'Телосложение',
    Ability.INTELLIGENCE: 'Интеллект',
    Ability.WISDOM: 'Мудрость',
    Ability.CHARISMA: 'Харизма',
}
