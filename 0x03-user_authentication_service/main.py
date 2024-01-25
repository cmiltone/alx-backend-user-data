#!/usr/bin/env python3
"""A simple end-to-end (E2E) integration test for `app.py`.
"""
import requests

BASE_URL = "http://0.0.0.0:5000"


def register_user(email: str, password: str) -> None:
    """test registration
    """
    url = "{}/users".format(BASE_URL)
    data = {
        'email': email,
        'password': password,
    }
    res = requests.post(url, data=data)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "user created"}
    res = requests.post(url, data=data)
    assert res.status_code == 400
    assert res.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """test login with a wrong password
    """
    url = "{}/sessions".format(BASE_URL)
    data = {
        'email': email,
        'password': password,
    }
    res = requests.post(url, data=data)
    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """test log in
    """
    url = "{}/sessions".format(BASE_URL)
    data = {
        'email': email,
        'password': password,
    }
    res = requests.post(url, data=data)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "logged in"}
    return res.cookies.get('session_id')


def profile_unlogged() -> None:
    """test fetching profile info while logged out
    """
    url = "{}/profile".format(BASE_URL)
    res = requests.get(url)
    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """test fetching profile info
    """
    url = "{}/profile".format(BASE_URL)
    cookies = {
        'session_id': session_id,
    }
    res = requests.get(url, cookies=cookies)
    assert res.status_code == 200
    assert "email" in res.json()


def log_out(session_id: str) -> None:
    """test log out of a session
    """
    url = "{}/sessions".format(BASE_URL)
    cookies = {
        'session_id': session_id,
    }
    res = requests.delete(url, cookies=cookies)
    assert res.status_code == 200
    assert res.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """test password reset request
    """
    url = "{}/reset_password".format(BASE_URL)
    data = {'email': email}
    res = requests.post(url, data=data)
    assert res.status_code == 200
    assert "email" in res.json()
    assert res.json()["email"] == email
    assert "reset_token" in res.json()
    return res.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """test update password
    """
    url = "{}/reset_password".format(BASE_URL)
    data = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password,
    }
    res = requests.put(url, data=data)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
