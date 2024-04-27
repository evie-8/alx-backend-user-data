#!/usr/bin/env python3
"""
Password encryption
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """creates a hashed password"""
    encoded_pasword = password.encode()
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates the provided password matches the hashed password """
    validated = False
    encoded_password = password.encode()
    if bcrypt.checkpw(encoded_password, hashed_password):
        validated = True
    return validated
