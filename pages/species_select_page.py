import streamlit as st
import constants.common
from character_creating_stages_menu import CharacterCreatingStagesMenu
from pages._base_page import BasePage


class SpeciesSelectPage(BasePage):
    SPECIES_KEY = 'species'

    def _change_species(self) -> None:
        print(st.session_state[self.SPECIES_KEY])

    def render(self) -> None:
        st.title('Выбор вида')
        st.text(
            'Мир невеличек как вы знаете населён множеством разумных маленьких животных у '
            'каждого из них свои особенности и сильные стороны.'
        )
        st.radio(
            label='Виды невеличек',
            options=['Кроты', 'Зайцы'],
            key=self.SPECIES_KEY,
            on_change=None,
        )
        st.image(image='./images/species_krot.png', caption='Крот')


SpeciesSelectPage().render()
CharacterCreatingStagesMenu().render()
