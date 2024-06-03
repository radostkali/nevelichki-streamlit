from enum import StrEnum, auto


class Skill(StrEnum):
    ACROBATICS = auto()
    VELICHKI_HANDLING = auto()
    AFFECT_COMPREHENSION = auto()
    ATHLETICS = auto()
    DECEPTION = auto()
    HISTORY = auto()
    PERSUASION = auto()
    SLEIGHT_OF_HANDS = auto()
    INSIGHT = auto()
    INVESTIGATION = auto()
    MEDICINE = auto()
    NATURE = auto()
    PERCEPTION = auto()
    PERFORMANCE = auto()
    RELIGION = auto()
    STEALTH = auto()
    SURVIVAL = auto()


SKILL_TO_NAME_MAP = {
    Skill.ACROBATICS: 'Акробатика (Лвк)',
    Skill.VELICHKI_HANDLING: 'Обращение с величками (Мдр)',
    Skill.AFFECT_COMPREHENSION: 'Понимание аффекта (Хар)',
    Skill.ATHLETICS: 'Атлетика (Сил)',
    Skill.DECEPTION: 'Обман (Хар)',
    Skill.HISTORY: 'История (Инт)',
    Skill.PERSUASION: 'Убеждение (Хар)',
    Skill.SLEIGHT_OF_HANDS: 'Ловкость рук (Лвк)',
    Skill.INSIGHT: 'Проницательность (Инт)',
    Skill.INVESTIGATION: 'Медицина (Мдр)',
    Skill.MEDICINE: 'Медицина (Мдр)',
    Skill.NATURE: 'Природа (Инт)',
    Skill.PERCEPTION: 'Внимание (Мдр)',
    Skill.PERFORMANCE: 'Выступление (Хар)',
    Skill.RELIGION: 'Религия (Инт)',
    Skill.STEALTH: 'Скрытность (Лвк)',
    Skill.SURVIVAL: 'Выживание (Мдр)',
}
