from typing import Annotated, Any
import pydantic
from . import enumerations

def validate(v: Any) -> Any:
    """
    This does nothing but triggers the error.
    """
    return v

class CookingModel(pydantic.BaseModel):
    fruit: Annotated[enumerations.FruitEnum, pydantic.BeforeValidator(validate)]