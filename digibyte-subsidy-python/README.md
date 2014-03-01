digibyte-subsidy-python
=====================

Python module for p2pool SUBSIDY_FUNC

- need boost-devel 
-  SUBSIDY_FUNC=lambda height: __import__('digibyte_subsidy').GetBlockBaseValue(height),


*  https://github.com/Rav3nPL/p2pool-rav/pull/21#issuecomment-33456471


# https://github.com/chaeplin/p2pool-drk
# SUBSIDY_FUNC=lambda nBits, height: __import__('darkcoin_subsidy').GetBlockBaseValue(nBits, height),
# subsidy=self.node.net.PARENT.SUBSIDY_FUNC(self.node.bitcoind_work.value['bits'].bits, self.node.bitcoind_work.value['height']),
# base_subsidy=self.node.net.PARENT.SUBSIDY_FUNC(self.current_work.value['bits'].bits, self.current_work.value['height']),

