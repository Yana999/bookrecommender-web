import json
import numpy as np
import pandas as pd
from bookRecommender import __version__ as model_version
from bookRecommender.predict import make_prediction
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger
from typing import Any

from app import __version__, schemas
from app.config import settings


api_router = APIRouter()


@api_router.get("/status", response_model=schemas.Status, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    status = schemas.Status(
        name=settings.PROJECT_NAME, api_version=__version__,
        model_version=model_version
    )
    return status.dict()


@api_router.post("/predict", response_model=[], status_code=200)
async def predict(input_data: schemas.BookRecommenderInput) -> Any:
    """
    Make predictions on the survival probability of the Titanic passengers
    """

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Making prediction on inputs: {input_data.input}")
    results = make_prediction(input_data=input_data.input)
    logger.info(f"Prediction result class: {results}")
    return results
