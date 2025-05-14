# Automated API test for "VerifyReferralCode" using pytest and requests

import requests
import pytest

BASE_URL = "https://apidev-poly.foodismconnect.com/api/v1"  # Replace with actual URL
# Test for Login API
@pytest.mark.parametrize("email, password, expected_status", [
    ("test@example.com", "correctpassword", 200),
    ("test@example.com", "wrongpassword", 401)
])
def test_login(email, password, expected_status):
    url = f"{BASE_URL}/Login"
    payload = {
        'email': email,
        'password': password,
        'device_type': "android",
        'device_token': "your_device_token_here"
    }
    response = requests.post(url, data=payload)

    assert response.status_code == expected_status

    data = response.json()
    assert 'success' in data
    assert 'message' in data

    if expected_status == 200:
        assert 'access_token' in data
        assert data['access_token']
    else:
        assert 'access_token' not in data or not data['access_token']