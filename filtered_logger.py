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
    """
    returns the log message obfuscated:

    Arguments:
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating all
    fields in the log line (message)
    The function should use a regex to replace occurrences of certain
    field values.
    filter_datum should be less than 5 lines long and use re.sub to perform the
    substitution with a single regex.
    """
    extract, replace = (ptrns["extract"], ptrns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
