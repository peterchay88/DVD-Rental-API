from sqlalchemy.orm import Mapped, mapped_column

from .base_table import Base


class FilmTable(Base):
    __tablename__ = "film"
    
    film_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    release_year: Mapped[int] = mapped_column(nullable=True)
    language_id: Mapped[int] = mapped_column(nullable=False)
    rental_duration: Mapped[int] = mapped_column(nullable=False)
    rental_rate: Mapped[float] = mapped_column(nullable=False)
    length: Mapped[int] = mapped_column(nullable=True)
    replacement_cost: Mapped[float] = mapped_column(nullable=False)
    rating: Mapped[str] = mapped_column(nullable=True)
    special_features: Mapped[str] = mapped_column(nullable=True)
    
    