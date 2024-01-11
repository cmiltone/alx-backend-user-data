#!/usr/bin/env python3
"""A module for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashes password using random salt """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Returns True if hashed password was formed
    from the given password.
    Or False otherwise
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)