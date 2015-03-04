#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test that when you take an IP address, encode it, and then decode it
again, it matches the original address. These tests are applicable to
all versions of Hipku, regardless of changes to the dictionaries or schema.
"""

from __future__ import absolute_import

from pyhipku import encode
from pyhipku import decode


def test_ipv4():
    assert decode(encode('0.0.0.0')) == '0.0.0.0'
    assert decode(encode('82.158.98.2')) == '82.158.98.2'
    assert decode(encode('255.255.255.255')) == '255.255.255.255'


def test_ipv6():
    assert decode(encode('0:0:0:0:0:0:0:0')) == '0:0:0:0:0:0:0:0'
    assert (decode(encode('2c8f:27aa:61fd:56ec:7ebe:d03a:1f50:475f')) ==
            '2c8f:27aa:61fd:56ec:7ebe:d03a:1f50:475f')
    assert (decode(encode('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')) ==
            'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')


def test_abbreviated_ipv6():
    assert decode(encode('::0')) == '0:0:0:0:0:0:0:0'
    assert decode(encode('0::')) == '0:0:0:0:0:0:0:0'
    assert decode(encode('0::0')) == '0:0:0:0:0:0:0:0'
    assert decode(encode('0:0::0:0')) == '0:0:0:0:0:0:0:0'
