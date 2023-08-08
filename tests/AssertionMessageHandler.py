import pytest


class AssertionMessageHandler:

    def __init__(self, text: str, result: bool):
        self.text = text
        self.result = result

        self.display_result()

    def display_result(self) -> None:
        if self.result:
            pytest.fail(self.text)
        else:
            assert f"{self.text}: {self.result}"
