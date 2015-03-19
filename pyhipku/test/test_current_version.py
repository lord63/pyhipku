#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test that a series of encoded test IPs match haiku for the current
set of dictionaries and schema, and that a series of decoded test
haiku match IPs for the current dictionaries and schema. These tests
must be updated whenever the dictionaries or schema are changed.
"""

from __future__ import absolute_import
import unittest

from pyhipku import encode
from pyhipku import decode


class PyhipkuTestCase(unittest.TestCase):
    def setUp(self):
        self.ipv4_pairs = [
            ['0.0.0.0', 'The agile beige ape\naches in the ancient canyon.\n'
             'Autumn colors blow.\n'],
            ['127.0.0.1', 'The hungry white ape\naches in the ancient canyon'
             '.\nAutumn colors crunch.\n'],
            ['82.158.98.2', 'The fearful blue newt\nwakes in the foggy desert'
             '.\nAutumn colors dance.\n'],
            ['255.255.255.255', 'The weary white wolf\nyawns in the '
             'wind-swept wetlands.\nYellowwood leaves twist.\n']
        ]
        self.ipv6_pairs = [
            ['0:0:0:0:0:0:0:0', 'Ace ants and ace ants\naid ace ace ace ace '
             'ace ants.\nAce ants aid ace ants.\n'],
            ['2c8f:27aa:61fd:56ec:7ebe:d03a:1f50:475f', 'Cursed mobs and '
             'crazed queens\nfeel wrong gruff tired moist slow sprats.\nFaint '
             'bulls dread fond fruits.\n'],
            ['ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'Young yaks and '
             'young yaks\ntend young young young young young yaks.\nYoung '
             'yaks tend young yaks.\n']
        ]

    def test_ipv4_encode(self):
        for i in range(len(self.ipv4_pairs)):
            self.assertEqual(encode(self.ipv4_pairs[i][0]),
                             self.ipv4_pairs[i][1])

    def test_ipv6_encode(self):
        for i in range(len(self.ipv6_pairs)):
            self.assertEqual(encode(self.ipv6_pairs[i][0]),
                             self.ipv6_pairs[i][1])

    def test_ipv4_decode(self):
        for i in range(len(self.ipv4_pairs)):
            self.assertEqual(decode(self.ipv4_pairs[i][1]),
                             self.ipv4_pairs[i][0])

    def test_ipv6_decode(self):
        for i in range(len(self.ipv6_pairs)):
            self.assertEqual(decode(self.ipv6_pairs[i][1]),
                             self.ipv6_pairs[i][0])

    def test_encode_exception_handle(self):
        self.assertRaises(ValueError, encode, 'Hello, world')
        self.assertRaises(ValueError, encode, '127.0.0.2560')
        self.assertRaises(ValueError, encode, '127.0.0')
        self.assertRaises(ValueError, encode, '0::0:zzzz')
        self.assertRaises(ValueError, encode, '0:0:0:0:0:0:0')

    def test_decode_exception_handle(self):
        self.assertRaises(ValueError, decode, 'Hello, world.')
        self.assertRaises(ValueError, decode,
                          ('The hungry white ape\naches in the ancient canyon.'
                           '\nAutumn colors foo.\n'))
