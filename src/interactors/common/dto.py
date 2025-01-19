from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class BaseDTO:
    def dict(self) -> dict[str, Any]:
        return {k: str(v) for k, v in asdict(self).items()}
