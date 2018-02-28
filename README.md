# coinbase-pricing-python

## Purpose

Another Python wrapper for Coinbase's Pricing API.  I wanted something modular and lightweight that I could then package into other projects.

## Roadmap

See [Projects Page](https://github.com/uilyam/coinbase-pricing-python/projects/1)

## Dependencies

Requests - To make HTTP GET requests to the Coinbase API.

## Getting Started

Add the following to the packages section of your [Pipenv's Pipfile](https://github.com/pypa/pipenv)

```text
cbp = {git = "https://github.com/uilyam/coinbase-pricing-python.git"}
```

## The Design

The basic idea for the library is to provide simple functions that require
mininmal configuration that will call down into more complex functions.  Thereby hiding implementation details from the user.  For example, the following function gets the current Spot price for Bitcoin denonminated in US Dollars.

```python
from cbp.btc import get_btc_spot
from cbp.constants import EXCHANGE_RATE_USD

get_btc_spot(EXCHANGE_RATE_USD)
```

Behind the scenes it will call a get_btc function which calls a get_price function.  At each level providing another variable that will eventually be used to construct the API request.

```text
get_btc_spot("USD") => get_btc("USD", "spot") => get_price("USD", "spot", "BTC")
```

## Examples

Examples for each currency can be found in the examples directory.

## Tests

In a terminal, run:

```bash
python -m unittest discover
```

## License - MIT

Copyright 2018 William Fleming

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
