from typing import Any


class BasePage:

    def render(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError
