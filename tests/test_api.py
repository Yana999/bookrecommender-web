import numpy as np
import pandas as pd
from fastapi.testclient import TestClient

import random

import json

def test_make_prediction(client: TestClient, test_data: str) -> None:
    # Given
    payload = {
        # ensure pydantic plays well with np.nan
        "input": test_data
    }

    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )


    print(payload)

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    print(prediction_data)
    assert isinstance(prediction_data, list)
