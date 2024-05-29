import streamlit as st
import constants.common


class CharacterCreatingStagesMenu:

    def render(self):
        st.sidebar.page_link(constants.common.PagesPaths.HELLO, label='Создаем невеличку!')
        st.sidebar.page_link(constants.common.PagesPaths.SPECIES_SELECT, label='1. Выбор вида')
        # if st.session_state.role in ['admin', 'super-admin']:
        #     st.sidebar.page_link('pages/admin.py', label='Manage users')
        #     st.sidebar.page_link(
        #         'pages/super-admin.py',
        #         label='Manage admin access',
        #         disabled=st.session_state.role != 'super-admin',
        #     )
