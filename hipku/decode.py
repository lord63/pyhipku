#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import lower

from dictionary import *


def decode(haiku):
    word_array = split_haiku(haiku)
    is_ipv6 = haiku_is_ipv6(word_array)
    factor_array = get_factors(word_array, is_ipv6)
    octet_array = get_octets(factor_array, is_ipv6)
    ip_string = get_ip_string(octet_array, is_ipv6)
    return ip_string


def split_haiku(haiku):
    word_array = lower(haiku).replace('.', '').split()
    return word_array


def haiku_is_ipv6(word_array):
    if word_array[0] == 'the':
        is_ipv6 = False
    else:
        is_ipv6 = True
    return is_ipv6


def get_key(is_ipv6):
    """Return an array of dictionaries representing the correct word
    order for the haiku"""
    if is_ipv6:
        key = [adjectives, nouns, adjectives, nouns, verbs, adjectives,
               adjectives, adjectives, adjectives, adjectives, nouns,
               adjectives, nouns, verbs, adjectives, nouns]
    else:
        key = [animal_adjectives, animal_colors, animal_nouns, animal_verbs,
               nature_adjectives, nature_nouns, plant_nouns, plant_verbs]
    return key


def get_factors(word_array, is_ipv6):
    key = get_key(is_ipv6)
    if is_ipv6:
        word_array.remove('and')
    else:
        word_array.remove('the')
        word_array.remove('in')
        word_array.remove('the')
        word_array.insert(6, ' '.join(word_array[6:-1]))
        del word_array[7:-1]

    factor_array = []
    for i in range(len(key)):
        factor_array.append(key[i].index(word_array[i]))
    return factor_array


def get_octets(factor_array, is_ipv6):
    if is_ipv6:
        multiplier = 256
    else:
        multiplier = 16
    octet_array = []
    for i in range(0, len(factor_array), 2):
        result = factor_array[i]*multiplier + factor_array[i+1]
        if is_ipv6:
            origin = hex(result)[2:]
        else:
            origin = str(result)
        octet_array.append(origin)
    return octet_array


def get_ip_string(octct_array, is_ipv6):
    if is_ipv6:
        separator = ':'
    else:
        separator = '.'
    ip_string = separator.join(octct_array)
    return ip_string