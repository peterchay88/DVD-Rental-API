from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)
from pydantic.alias_generators import to_camel


class ActorRead(BaseModel):

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )

    id: int = Field(validation_alias="actor_id")
    first_name: str
    last_name: str
