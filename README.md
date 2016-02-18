                                   NACCulator

[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.46253.svg)](http://dx.doi.org/10.5281/zenodo.46253)

Converts a CSV data file exported from REDCap into the NACC's UDS3 fixed-width
format.

FILES
-----

This is not exhaustive, but here is an explanation of some important files.

nacc/:
    Top-level Python package for all things NACC.

nacc/redcap2nacc.py:
    converts a CSV data file exported from REDCap into NACC's UDS3 fixed-width
    format

nacc/uds3/blanks.py:
    specialized library for "Blanking Rules"

nacc/uds3/ivp/forms.py:
    UDS3 IVP forms represented as Python classes

tools/generator.py:
    generates Python objects based on NACC Data Element Dictionaries in CSV


HOWTO Convert from REDCap to NACC
---------------------------------

    $ pip install nacculator
    $ redcap2nacc < data.csv > data.nacc

Manually:
    $ PYTHONPATH=. ./nacc/redcap2nacc.py data.csv > data.nacc

Note: output is written to STDOUT; errors are written to STDERR; input can be
      STDIN or the first argument passed to redcap2nacc.

HOWTO Generate New Forms
------------------------

Note: executing generator.py from within tools is an important step as the
      script assumes any corrected DEDs are stored under a folder in the
      current working directory called 'corrected'.

Warning: read the warnings in the current ../nacc/uds3/ivp/forms.py first.

    $ cd tools
    $ PYTHONPATH=.. ./generator.py uds3/ded/csv/ > ../nacc/uds3/ivp/forms.py
    $ edit ../nacc/uds3/ivp/forms