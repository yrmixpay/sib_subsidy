from distutils.core import setup, Extension

darkcoin_module = Extension('darkcoin_subsidy', sources = ['darkcoin_subsidy.cpp'])

setup (name = 'darkcoin_subsidy',
       version = '1.1',
       description = 'Subsidy function for Darkcoin',
       ext_modules = [darkcoin_module])
