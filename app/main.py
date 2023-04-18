from __future__ import annotations
from typing import Any


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        if isinstance(other, int | float):
            km = self.km + other
        else:
            km = self.km + other.km
        return Distance(km)

    def __iadd__(self, other: Any) -> Distance:
        if isinstance(other, int | float):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: Any) -> Distance:
        return Distance(km=self.km * other)

    def __truediv__(self, other: Any) -> Distance | None:
        if isinstance(other, int | float):
            km = round(self.km / other, 2)
        else:
            return None
        return Distance(km)

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, int | float):
            return self.km < other
        else:
            return self.km < other.km

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, int | float):
            return self.km > other
        else:
            return self.km > other.km

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, int | float):
            return self.km == other
        else:
            return self.km == other.km

    def __le__(self, other: Any) -> bool:
        if isinstance(other, int | float):
            return self.km <= other
        else:
            return self.km <= other.km

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, int | float):
            return self.km >= other
        else:
            return self.km >= other.km
