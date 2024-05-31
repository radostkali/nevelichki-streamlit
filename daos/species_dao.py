import constants.abilities
import constants.species
import data.species
from entities import SpeciesEntity


class SpeciesDAO:

    def get_species(self, species: constants.species.Species) -> SpeciesEntity:
        match species:
            case constants.species.Species.MOLE:
                return data.species.SPECIES_ENTITY_MOLE
            case constants.species.Species.HARE:
                return data.species.SPECIES_ENTITY_HARE
            case constants.species.Species.CAT:
                return data.species.SPECIES_ENTITY_CAT
            case constants.species.Species.PARROT:
                return data.species.SPECIES_ENTITY_PARROT
            case constants.species.Species.RAT:
                return data.species.SPECIES_ENTITY_RAT
            case constants.species.Species.BADGER:
                return data.species.SPECIES_ENTITY_BADGER
            case constants.species.Species.ARCTIC_FOX:
                return data.species.SPECIES_ENTITY_ARCTIC_FOX
            case constants.species.Species.PENGUIN:
                return data.species.SPECIES_ENTITY_PENGUIN

