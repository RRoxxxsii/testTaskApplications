import dataclasses


@dataclasses.dataclass(frozen=True)
class LimitOffset:
    limit: int
    offset: int


class LimitOffsetPaginator:
    def __init__(self, page: int, size: int):
        self.page = page
        self.size = size

    def _find_limit(self) -> int:
        return self.size

    def _find_offset(self) -> int:
        return (self.page - 1) * self.size

    def execute(self) -> LimitOffset:
        return LimitOffset(
            limit=self._find_limit(), offset=self._find_offset()
        )
