import datetime
from typing import Annotated

from sqlalchemy import BigInteger, DateTime, Identity, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

intpk = Annotated[  # noqa
    int,
    mapped_column(BigInteger, Identity(start=1, cycle=True), primary_key=True),
]


time_created = Annotated[
    datetime.datetime,
    mapped_column(DateTime(timezone=True), server_default=func.now()),
]


class AbstractModel(DeclarativeBase):
    _repr_cols_num: int = 3
    _repr_cols: tuple = tuple()

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self._repr_cols or idx < self._repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")
        return f"<{self.__class__.__name__} {', '.join(cols)}>"


class ApplicationORM(AbstractModel):
    __tablename__ = "applications"

    id: Mapped[intpk]
    user_name: Mapped[str] = mapped_column(
        String(length=40), nullable=False, index=True
    )
    description: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[time_created]
