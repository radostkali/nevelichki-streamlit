from dataclasses import dataclass

from entities import SpeciesEntity, SpeciesAbilitiesBonus


@dataclass(slots=True)
class CharacterStateEntity:
    species: SpeciesEntity | None = None
    species_abilities_bonus: SpeciesAbilitiesBonus | None = None
