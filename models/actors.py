from pydantic import (
    BaseModel,
    ConfigDict
)
from pydantic.alias_generators import to_camel


class Actor(BaseModel):

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    id: int
    first_name: str
    last_name: str

