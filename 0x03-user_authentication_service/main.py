#!/usr/bin/env python3
"""
End-to-end integration test
"""


def register_user(email: str, password: str) -> None:
    """Testing for registered user
    """
    assert True


def log_in_wrong_password(email: str, password: str) -> None:
    """Login for wrong password test
    """
    assert True


def log_in(email: str, password: str) -> str:
    """Test for login
    """
    assert True


def profile_unlogged() -> None:
    """profile unlogged test
    """
    assert True


def profile_logged(session_id: str) -> None:
    """profile logged in test
    """
    assert True


def log_out(session_id: str) -> None:
    """logout test
    """
    assert True


def reset_password_token(email: str) -> str:
    """reset password test
    """
    assert True


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test for update password
    """
    assert True


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
