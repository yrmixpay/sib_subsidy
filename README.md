darkcoin_subsidy (python) v1.2
==============================

Python module for Darkcoin's subsidy function.

Currently to be used for:

* p2pool-drk (SUBSIDY_FUNC)
* darkcoind-ncurses (block_subsidy)


Install
-------

Python 2.7 is required as well as a gcc with c++ bindings.

    $ sudo python2 setup.py install

Or use pip:

    $ pip install darkcoin_subsidy

[pypi.python.org/pypi/darkcoin_subsidy](https://pypi.python.org/pypi/darkcoin_subsidy)

Usage
-----

Import the module and call the function:

    import darkcoin_subsidy as ds

    nBits = 469894998
    nHeight = 21288
    print ds.GetBlockBaseValue(nBits, nHeight)

Testnet:

    print ds.GetBlockBaseValue_testnet(nBits, nHeight)


Credits
-------

* Module written by @chaeplin https://github.com/chaeplin/SUBSIDY_FUNC
* Module maintained by @dstorm https://bitbucket.org/dstorm/p2pool-drk
* Module maintained by @vertoe https://github.com/vertoe/darkcoin_subsidy
