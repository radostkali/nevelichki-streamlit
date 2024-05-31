import streamlit as st
import constants.species
import constants.common
from character_creating_stages_menu import CharacterCreatingStagesMenu
from daos import SpeciesDAO
from daos.character_state_dao import CharacterStateDao
from entities import SpeciesAbilitiesBonus
from pages.page_renderer import BasePage, PageRenderer


class SpeciesSelectPage(BasePage):
    SPECIES_KEY = '_species'
    SPECIES_ABILITIES_BONUS_KEY = '_species_bonus'

    def __init__(self, species_dao: SpeciesDAO, character_state_dao: CharacterStateDao) -> None:
        self._species_dao = species_dao
        self._character_state_dao = character_state_dao

    def _render_additional_features(self, additional_features: list[str]) -> None:
        additional_features_strings = []
        for i, additional_feature in enumerate(additional_features, start=1):
            additional_features_strings.append(f'{i}. {additional_feature}')

        st.markdown('\n'.join(additional_features_strings), unsafe_allow_html=True)

    def _get_ability_bonus_string(self, abilities_bonus: SpeciesAbilitiesBonus) -> str:
        abilities_bonus_strings = []
        for ability_bonus in abilities_bonus.abilities_bonuses:
            ability_bonus_string = f'+{ability_bonus.bonus} {ability_bonus.name}'
            abilities_bonus_strings.append(ability_bonus_string)

        return f'**{", ".join(abilities_bonus_strings)}**'

    def _render_species_bonuses_select(self, species_abilities_bonuses: list[SpeciesAbilitiesBonus]) -> None:
        st.radio(
            label='Выберете бонус вида:',
            options=species_abilities_bonuses,
            key=self.SPECIES_ABILITIES_BONUS_KEY,
            index=None,
            format_func=self._get_ability_bonus_string,
        )

    def _render_species(self, species: constants.species.Species) -> None:
        species_entity = self._species_dao.get_species(species=species)
        st.markdown(f'#### {species_entity.name}')
        st.markdown(f'<span style="color: #bcbcbc">{species_entity.description}</span>', unsafe_allow_html=True)
        st.markdown('##### 1. Увеличение характеристик')
        self._render_species_bonuses_select(species_abilities_bonuses=species_entity.species_abilities_bonuses)
        st.markdown('##### 2. Размер')
        st.markdown(species_entity.size_description, unsafe_allow_html=True)
        st.markdown('##### 3. Скорость')
        st.markdown(f'Ваша базовая скорость перемещения составляет **{species_entity.speed_in_meters} метров**.')
        st.markdown('##### 4. Языки')
        st.markdown(species_entity.languages_description, unsafe_allow_html=True)
        st.markdown('##### 5. Дополнительные особенности')
        self._render_additional_features(additional_features=species_entity.additional_features)

        current_ability_bonus = st.session_state[self.SPECIES_ABILITIES_BONUS_KEY]
        is_ability_bonus_selected = current_ability_bonus is not None

        _, _, center, _, _ = st.columns(5)
        with center:
            if st.button(
                label='Далее',
                help=None if is_ability_bonus_selected else 'Выберите бонус вида',
                disabled=not is_ability_bonus_selected,
            ):
                self._character_state_dao.set_character_species(
                    species=species_entity,
                    species_ability_bonus=current_ability_bonus,
                )
                st.switch_page(constants.common.PagesPath.SPECIES_SELECT)

        st.image(image=species_entity.image_path)

    def _on_species_select_callback(self) -> None:
        st.session_state[self.SPECIES_ABILITIES_BONUS_KEY] = None

    def render_content(self) -> None:
        st.title('1. Выбор вида')
        st.markdown(
            '> <span style="color: #999999">Мир невеличек как вы знаете населён множеством разумных маленьких животных у '
            'каждого из них свои особенности и сильные стороны.</span>',
            unsafe_allow_html=True,
        )
        st.radio(
            label='Выберете вид невелички:',
            help='Нажмите на вид, чтобы ознакомится с его историей, особенностями и характеристиками.',
            options=[str(i) for i in constants.species.Species],
            key=self.SPECIES_KEY,
            index=None,
            format_func=lambda option: constants.species.SPECIES_TO_NAME_MAP[option],
            on_change=self._on_species_select_callback,
        )
        current_species = st.session_state[self.SPECIES_KEY]
        if current_species:
            self._render_species(species=current_species)


page = SpeciesSelectPage(
    species_dao=SpeciesDAO(),
    character_state_dao=CharacterStateDao(),
)
PageRenderer(
    character_state_dao=CharacterStateDao(),
    character_creating_stages_menu=CharacterCreatingStagesMenu(),
).render(page=page)
