import streamlit as st
import constants.common
from character_creating_stages_menu import CharacterCreatingStagesMenu
from pages._base_page import BasePage


class HelloPage(BasePage):

    def _on_create_button_callback(self):
        st.switch_page(constants.common.PagesPaths.SPECIES_SELECT)

    def render(self) -> None:
        st.title('НЕВЕЛИЧКИ & ВЕЛИЧКИ')
        st.text('Приветствую тебя, ВЕЛИЧКА, на странице создания листа НЕВЕЛИЧКИ!')
        st.image(image='./images/start.png')
        _, _, center, _, _ = st.columns(5)
        with center:
            st.text('\n\n\n')
            st.page_link(
                page=constants.common.PagesPaths.SPECIES_SELECT,
                label='Создать',
                icon="🐰",
            )


HelloPage().render()
CharacterCreatingStagesMenu().render()
