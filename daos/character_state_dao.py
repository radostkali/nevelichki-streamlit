import streamlit as st
import constants.common
from entities import CharacterStateEntity, SpeciesEntity, SpeciesAbilitiesBonus


class CharacterStateDao:

    class StateDoesNotInitialized(Exception):
        ...

    def _get_character_state(self) -> CharacterStateEntity:
        try:
            character_state = st.session_state[constants.common.STATE_KEY_CHARACTER]
        except KeyError:
            raise self.StateDoesNotInitialized

        if not isinstance(character_state, CharacterStateEntity):
            raise self.StateDoesNotInitialized

        return character_state

    def _set_state(self, character_state: CharacterStateEntity) -> None:
        st.session_state[constants.common.STATE_KEY_CHARACTER] = character_state

    def init_character_state(self) -> None:
        if constants.common.STATE_KEY_CHARACTER not in st.session_state:
            self._set_state(character_state=CharacterStateEntity())

    def get_character_state(self) -> CharacterStateEntity:
        return self._get_character_state()

    def set_character_species(self, species: SpeciesEntity, species_ability_bonus: SpeciesAbilitiesBonus) -> None:
        character_state = self._get_character_state()
        character_state.species = species
        character_state.species_abilities_bonus = species_ability_bonus
        character_state.creating_stages_done.add(constants.common.CharacterCreatingStage.SPECIES_SELECT)
        self._set_state(character_state=character_state)
