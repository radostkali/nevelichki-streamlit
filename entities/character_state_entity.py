from dataclasses import dataclass, field

from entities import SpeciesEntity, SpeciesAbilitiesBonus


@dataclass(slots=True)
class CharacterStateEntity:

    creating_stages_done: set[str] = field(default_factory=set)

    species: SpeciesEntity | None = None
    species_abilities_bonus: SpeciesAbilitiesBonus | None = None

