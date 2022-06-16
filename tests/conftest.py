from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from bookRecommender.config.core import config
from bookRecommender.processing.data_manager import load_dataset

from app.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    return '16 Lighthouse Road'


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}