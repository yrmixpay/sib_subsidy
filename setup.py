from distutils.core import setup, Extension

darkcoin_subsidy_module = Extension('darkcoin_subsidy', sources = ['darkcoin_subsidy.cpp'])

setup (name = 'darkcoin_subsidy',
       version = '1.2',
       description = 'Subsidy function for Darkcoin',
       ext_modules = [darkcoin_subsidy_module])
