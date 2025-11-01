from typing import Protocol, Iterable

class DataAPI(Protocol):
    def list_series(self) -> Iterable[str]:...
