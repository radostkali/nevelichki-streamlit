import streamlit as st
import constants.common


class CharacterCreatingStagesMenu:

    def render(self):
        st.sidebar.page_link(constants.common.PagesPath.HELLO, label='Создаем невеличку!')
        st.sidebar.page_link(constants.common.PagesPath.SPECIES_SELECT, label='1. Выбор вида')
