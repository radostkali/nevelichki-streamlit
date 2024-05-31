from typing import Any

from character_creating_stages_menu import CharacterCreatingStagesMenu
from daos.character_state_dao import CharacterStateDao


class BasePage:

    def render_content(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError


class PageRenderer:

    def __init__(
            self,
            character_state_dao: CharacterStateDao,
            character_creating_stages_menu: CharacterCreatingStagesMenu,
    ) -> None:
        self._character_state_dao = character_state_dao
        self._character_creating_stages_menu = character_creating_stages_menu

    def __init_state(self) -> None:
        self._character_state_dao.init_character_state()

    def render(self, page: BasePage) -> None:
        self.__init_state()
        self._character_creating_stages_menu.render()
        page.render_content()
