#!/usr/bin/env python3
"""module declares functions"""
import os
import re
import logging
# import mysql.connector
from typing import List

ptrns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}

FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """returns the log message obfuscated:"""
    extract, replace = (ptrns["extract"], ptrns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
