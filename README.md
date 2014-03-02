

NAME="Ubuntu"
VERSION="12.04.4 LTS, Precise Pangolin"

git clone https://github.com/chaeplin/SUBSIDY_FUNC.git

cd SUBSIDY_FUNC/digibyte-subsidy-python/

python setup.py install

:if get err -> apt-get install libboost1.48-all-dev 

python test.py 

:work ? then

edit p2pool/bitcoin/network.py

replace 

SUBSIDY_FUNC=~~~

to

SUBSIDY_FUNC=lambda height: import('digibyte_subsidy').GetBlockBaseValue(height),

