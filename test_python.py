from flask import Flask
import pytest

from python import app  # Replace "myapp" with the name of your Flask app modulep

def test_Hello_world():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data == b'hello world'
