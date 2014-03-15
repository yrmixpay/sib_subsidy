darkcoin-subsidy-python
=====================

Python module for p2poll-drk SUBSIDY_FUNC


- need boost-devel 



*  https://github.com/Rav3nPL/p2pool-rav/pull/21#issuecomment-33456471


-SUBSIDY_FUNC=lambda nBits, height: __import__('darkcoin_subsidy').GetBlockBaseValue(nBits, height),

-subsidy=self.node.net.PARENT.SUBSIDY_FUNC(self.node.bitcoind_work.value['bits'].bits, self.node.bitcoind_work.value['height']),

-base_subsidy=self.node.net.PARENT.SUBSIDY_FUNC(self.current_work.value['bits'].bits, self.current_work.value['height']),

