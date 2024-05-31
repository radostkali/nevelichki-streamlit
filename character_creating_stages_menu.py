import streamlit as st
import constants.common
from daos.character_state_dao import CharacterStateDao


class CharacterCreatingStagesMenu:

    def __init__(
            self,
            character_state_dao: CharacterStateDao,
    ) -> None:
        self._character_state_dao = character_state_dao

    def render(self):
        st.sidebar.page_link(constants.common.PagesPath.HELLO, label='Создаем невеличку!')

        character_state = self._character_state_dao.get_character_state()
        if constants.common.CharacterCreatingStage.SPECIES_SELECT not in character_state.creating_stages_done:
            st.sidebar.page_link(constants.common.PagesPath.SPECIES_SELECT, label='🐰 Выбор вида')
            return

        st.sidebar.page_link(constants.common.PagesPath.SPECIES_SELECT, label='✅ Выбор вида')
        st.sidebar.page_link(constants.common.PagesPath.CLASS_SELECT, label='🛠️ Выбор класса')
