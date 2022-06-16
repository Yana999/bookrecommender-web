import json
import numpy as np
import pandas as pd
import random
from fastapi.testclient import TestClient


def test_make_prediction(client: TestClient, test_data: str) -> None:
    # Arrange
    payload = {
        # ensure pydantic plays well with np.nan
        "input": test_data
    }

    # Apply
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )
    print(payload)

    # Assert
    assert response.status_code == 200
    prediction_data = response.json()
    print(prediction_data)
    assert isinstance(prediction_data, list)
