import streamlit as st
import constants.common
from character_creating_stages_menu import CharacterCreatingStagesMenu
from daos.character_state_dao import CharacterStateDao
from pages.page_renderer import BasePage, BasePageRenderer, PageRenderer


class HelloPage(BasePage):

    def render_content(self) -> None:
        st.title('НЕВЕЛИЧКИ & ВЕЛИЧКИ')
        st.markdown('> *Приветствую тебя, ВЕЛИЧКА, на странице создания листа НЕВЕЛИЧКИ!*')
        st.markdown(
            'Первые шаги в жизни исследователя целого мира невеличек начинаются с простого вопроса...  '
            '**А кто я?**'
        )
        st.markdown('Вопрос это обширный и включает в мире невеличек  следующие подпункты:')
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

        _, _, center, _, _ = st.columns(5)
        with center:
            if st.button(label='🐰 Создать'):
                st.switch_page(constants.common.PagesPath.SPECIES_SELECT)

        st.image(image='./images/main_cat.png')


PageRenderer(
    character_state_dao=CharacterStateDao(),
).render(
    page=HelloPage(),
)
CharacterCreatingStagesMenu().render()
