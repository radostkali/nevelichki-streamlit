import streamlit as st
import constants.common
from character_creating_stages_menu import CharacterCreatingStagesMenu
from daos.character_state_dao import CharacterStateDao
from pages.page_renderer import BasePage, PageRenderer


class HelloPage(BasePage):

    def render_content(self) -> None:
        st.title('НЕВЕЛИЧКИ & ВЕЛИЧКИ')
        st.markdown(
            '> <span style="color: #999999">Приветствую тебя, ВЕЛИЧКА, на странице создания листа НЕВЕЛИЧКИ!</span>',
            unsafe_allow_html=True,
        )
        st.markdown(
            'Первые шаги в жизни исследователя целого мира невеличек начинаются с простого вопроса...  '
            '**А кто я?** Вопрос это обширный и включает в мире невеличек  следующие подпункты:'
        )
        st.markdown('#### 1. Выбор вида')
        st.markdown(
            'Мир невеличек как вы знаете населён множеством разумных маленьких животных у каждого из них свои '
            'особенности и сильные стороны.'
        )
        st.markdown('#### 2. Выбор класса')
        st.markdown(
            'Невелички которые занимаются исследованием целого мира и его секретов всегда обладают особенными '
            'умениями отличающими их от простых обывателей и помогающие в приключениях.'
        )
        st.markdown('#### 3. Определение характеристик')
        st.markdown(
            'Здесь вы выбираете в чем ваш персонаж хорош, например он силен и ловок, а в чем он не так хорош.'
        )
        st.markdown('#### 4. Описание предыстории')
        st.markdown(
            'Всегда важно, кем был/а невеличка до начала его/её нового приключения и что толкнула её в него.'
        )
        st.markdown('#### 5. Выбор снаряжения')
        st.markdown(
            'Что вы взяли с собой в путешествие, только оружие, когда сбегали из дома? '
            'Возможно все, что у вас есть это фамильный перстень?'
        )

        _, center, _ = st.columns(3)
        with center:
            if st.button(label='🐰 Создать персонажа'):
                st.switch_page(constants.common.PagesPath.SPECIES_SELECT)

        st.image(image='./images/main_cat.png')


PageRenderer(
    character_state_dao=CharacterStateDao(),
    character_creating_stages_menu=CharacterCreatingStagesMenu(
        character_state_dao=CharacterStateDao(),
    ),
).render(
    page=HelloPage(),
)
