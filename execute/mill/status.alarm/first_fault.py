
##########################################################################################################################

# Imports
from os import path
from sys import argv
from json import loads, dump

# Modules
from prevent_billet import cause

##########################################################################################################################
#                                                      PDA MILL STATUS                                                   #
##########################################################################################################################

# Get Input Params
data = loads(argv[1])

# Check Received Data
text = cause(data=data, status='gap_off')
if not isinstance(text, str) or text == '':
    raise Exception('invalid argument "data"')

# Get Target JSON
fileDir = path.dirname(path.abspath(__file__))
pbPath = path.abspath(path.join(fileDir, './prevent_billet.json'))

# Write to JSON File
dump(data, open(pbPath, 'w'), indent=2)

##########################################################################################################################

    
