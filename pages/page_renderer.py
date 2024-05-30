from typing import Any

from daos.character_state_dao import CharacterStateDao


class BasePage:

    def render_content(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError


class PageRenderer:

    def __init__(
            self,
            character_state_dao: CharacterStateDao,
    ) -> None:
        self._character_state_dao = character_state_dao

    def __init_state(self) -> None:
        self._character_state_dao.init_character_state()

    def render(self, page: BasePage) -> None:
        self.__init_state()
        page.render_content()
