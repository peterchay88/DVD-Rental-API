from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class FilmRead(BaseModel):
    """Schema for reading film data"""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )

    film_id: int
    title: str
    description: str | None
    release_year: int | None
    language_id: int
    original_language_id: int | None
    rental_duration: int
    rental_rate: float
    length: int | None
    replacement_cost: float
    rating: str | None
    special_features: str | None