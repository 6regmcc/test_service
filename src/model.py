from sqlalchemy.orm import MappedColumn, Mapped
from sqlalchemy.testing.schema import mapped_column

from db_connection import Base


class Note(Base):
    __tablename__ = "note"
    id: Mapped[int] = mapped_column(primary_key=True)
    note_a: Mapped[str] = mapped_column()
    note_b: Mapped[str] = mapped_column()
