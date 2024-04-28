#!/usr/bin/env python3
"""Authentication module
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """API authentication management class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """validates if end point requires authentication"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        length_path = len(path)
        if length_path == 0:
            return True

        slash_path = True if path[length_path - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            if exc[l_exc - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:l_exc - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorization header handler"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates the current user """
        return None

    def session_cookie(self, request=None):
        """ Returns request cookie value """
        if request is None:
            return None
        cookie = getenv('SESSION_NAME')
        return request.cookies.get(cookie)
