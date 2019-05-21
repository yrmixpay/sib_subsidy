yrmix_subsidy (v1.3)
==============================

Python module for Yrmixcoin's subsidy function.

Currently to be used for:

* p2pool-yrmix (SUBSIDY_FUNC)
* yrmixcoind-ncurses (block_subsidy)


Install
-------

Python 2.7 is required as well as a gcc with c++ bindings.

    $ python setup.py install


Usage
-----

Import the module and call the function:

    import yrmix_subsidy as ds

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
* Module maintained by @jakehaas https://github.com/jakehaas/dash_subsidy
* Module maintained by @ivansib https://github.com/ivansib/sib_subsidy
