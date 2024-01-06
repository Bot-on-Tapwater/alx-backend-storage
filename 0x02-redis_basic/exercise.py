#!/usr/bin/env python3
"""Implement class Cache"""

import redis
import uuid
from typing import Dict


class Cache:
    """Class Cache"""

    def __init__(self):
        """
        Initializes an instance of the class.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """
        A description of the entire function
        its parameters, and its return types.
        """
        random_key = str(uuid.uuid4())

        self._redis.set(random_key, data)

        return random_key
