from dataclasses import dataclass
import constants.abilities
import constants.species


@dataclass(frozen=True, slots=True)
class SpeciesAbilityBonus:
    """ Бонус к конкретной характеристике """
    key: constants.abilities.Ability
    bonus: int

    @property
    def name(self) -> str:
        return constants.abilities.ABILITY_TO_NAME_MAP[self.key]


@dataclass(frozen=True, slots=True)
class SpeciesAbilitiesBonus:
    """ Варианты бонусов к характеристикам для вида невелички """
    abilities_bonuses: list[SpeciesAbilityBonus]


@dataclass(frozen=True, slots=True)
class SpeciesEntity:
    """ Вид невелички. Например: крот или кот. """

    key: constants.species.Species
    description: str
    species_abilities_bonuses: list[SpeciesAbilitiesBonus]
    size_description: str
    speed_in_meters: int
    languages_description: str
    additional_features: list[str]
    image_path: str

    @property
    def name(self) -> str:
        return constants.species.SPECIES_TO_NAME_MAP[self.key]
