from typing import Any


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        return f"Welcome to {self.name}"