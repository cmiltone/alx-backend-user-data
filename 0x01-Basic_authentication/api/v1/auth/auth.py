#!/usr/bin/env python3
""" Module for Auth clss
"""
import re
from flask import request
from typing import List, TypeVar


class Auth:
    """authentication implementation"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """auth guard"""
        if excluded_paths is not None and path is not None:
            for ex_path in map(lambda x: x.strip(), excluded_paths):
                _str = ''
                if ex_path[-1] == '*':
                    _str = '{}.*'.format(ex_path[0:-1])
                elif ex_path[-1] == '/':
                    _str = '{}/*'.format(ex_path[0:-1])
                else:
                    _str = '{}/*'.format(ex_path)
                if re.match(_str, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """gets auth header"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """gets current user"""
        return None
