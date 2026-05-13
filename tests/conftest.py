import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module

ORIGINAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture
def isolated_activities(monkeypatch):
    monkeypatch.setattr(app_module, "activities", copy.deepcopy(ORIGINAL_ACTIVITIES))
    return app_module.activities


@pytest.fixture
def client(isolated_activities):
    return TestClient(app_module.app)
