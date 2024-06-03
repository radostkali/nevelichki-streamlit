from dataclasses import dataclass
import constants.abilities
import constants.classes
import constants.skills


@dataclass(frozen=True, slots=True)
class ClassEntity:

    key: constants.classes.Class
    description: str
    main_ability: constants.abilities.Ability
    saving_throws_bonus_abilities: list[constants.abilities.Ability]
    start_hp: int
    armor: str
    weapons: str
    proficiency_bonus: int
    available_skills: list[constants.skills.Skill]
    image_path: str

    @property
    def name(self) -> str:
        return constants.skills.SKILL_TO_NAME_MAP[self.key]
