import streamlit as st
import constants.species
import constants.common
from character_creating_stages_menu import CharacterCreatingStagesMenu
from daos import SpeciesDAO
from daos.character_state_dao import CharacterStateDao
from entities import SpeciesAbilitiesBonus, SpeciesEntity
from pages.page_renderer import BasePage, PageRenderer


class ClassSelectPage(BasePage):

    def __init__(self, species_dao: SpeciesDAO, character_state_dao: CharacterStateDao) -> None:
        self._species_dao = species_dao
        self._character_state_dao = character_state_dao

    def render_content(self) -> None:
        st.title('2. Выбор класса')


page = ClassSelectPage(
    species_dao=SpeciesDAO(),
    character_state_dao=CharacterStateDao(),
)
PageRenderer(
    character_state_dao=CharacterStateDao(),
    character_creating_stages_menu=CharacterCreatingStagesMenu(
        character_state_dao=CharacterStateDao(),
    ),
).render(page=page)
