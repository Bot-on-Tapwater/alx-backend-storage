#!/usr/bin/env python3
"""Implement class Cache"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Class Cache"""

    def __init__(self):
        """
        Initializes a new instance of the class.

        Parameters:
            None

        Returns:
            None
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis and returns a random key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.
            It can be a string, bytes, integer, or float.

        Returns:
            str: A randomly generated key that is used
            to retrieve the stored data from Redis.
        """
        random_key = str(uuid.uuid4())

        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int]:
        """
        Retrieves the value associated with the specified key from the Redis cache.

        Parameters:
            key (str): The key to retrieve the value for.
            fn (Optional[Callable]): An optional function to apply to the retrieved value before returning it. Defaults to None.

        Returns:
            Union[str, bytes, int]: The value associated with the key. If the value is not found or fn is not provided, the raw value is returned.
        """
        value = self.redis_client.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        else:
            return value

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieves a string value from the cache using the specified key.

        Parameters:
            key (str): The key used to retrieve the value from the cache.

        Returns:
            Union[str, None]: The string value associated with the key in the cache,
            or None if the key is not found.
        """
        return self.get(key, fn=decode_utf8)

    def get_int(self, key: str) -> Union[int, None]:
        """
        Get the integer value associated with the given key.

        Args:
            key (str): The key to look up in the dictionary.

        Returns:
            Union[int, None]: The integer value associated with the key, or None if the key does not exist or the value cannot be converted to an integer.
        """
        return self.get(key, fn=int)
