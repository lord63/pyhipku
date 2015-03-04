# PyHipku

[![Latest Version][1]][2]
[![Build Status][3]][4]
[![Coverage Status][5]][6]

A tiny python library to encode IPv6 and IPv4 addressed as haiku.
This a python port of [hipku][7](javascript).

## Install

    $ pip install pyhipku

## Usage

Encode the IP address to haiku

    >>> from pyhipku import encode
    >>> print encode('127.0.0.1')
    The hungry white ape
    aches in the ancient canyon.
    Autumn colors crunch.

Decode haiku to IP address

    >>> from pyhipku import decode
    >>> decode('The hungry white ape\naches in the ancient canyon.\nAutumn colors crunch.\n')
    '127.0.0.1'

## License

MIT


[1]: http://img.shields.io/pypi/v/pyhipku.svg
[2]: https://pypi.python.org/pypi/pyhipku
[3]: https://travis-ci.org/lord63/pyhipku.svg
[4]: https://travis-ci.org/lord63/pyhipku
[5]: https://coveralls.io/repos/lord63/pyhipku/badge.svg
[6]: https://coveralls.io/r/lord63/pyhipku
[7]: https://github.com/gabemart/hipku
