from app import app

import pytest


@pytest.fixture
def client():
    return app.test_client()


def test_ping(client):
    resp=client.get('/ping')
    assert resp.text=='This is ping'


def test_predit(client):
    test_data={
    "Gender": "Male",
    "Married": "Unmarried",
    "ApplicantIncome": 5000000,
    "Credit_History": "Cleared Debts",
    "LoanAmount": 500000
}

    resp=client.get('/predict' , json=test_data)
    
    assert resp.text=='Rejected'