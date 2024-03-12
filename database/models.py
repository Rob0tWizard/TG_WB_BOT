from datetime import datetime

from sqlalchemy import DateTime, Integer, func, Column

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class InfoFromDb(Base):
    __tablename__ = 'info_from_db'

    id: Mapped[int]= mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    time: Mapped[datetime]= mapped_column(DateTime, default=func.now())
    vendor: Mapped[int] = mapped_column(Integer, nullable=False)
