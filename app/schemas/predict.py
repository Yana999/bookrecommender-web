from typing import Any, List, Optional

from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    preds: Optional[List[str]]


class BookRecommenderInput(BaseModel):
    input: str

    class Config:
        schema_extra = {
            "example": {
                "input": '16 Lighthouse Road'
            }
        }