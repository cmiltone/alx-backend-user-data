#!/usr/bin/env python3
""" Module for Auth clss
"""
from flask import request
from typing import List, TypeVar


class AUth:
    """authentication implementation"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """auth guard"""
        return False

    def authorization_header(self, request=None) -> str:
        """gets auth header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """gets current user"""
        return None
