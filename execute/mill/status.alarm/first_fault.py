
##########################################################################################################################

# Imports
import os
import sys
import json

# Modules
from . import prevent_billet

##########################################################################################################################
#                                                      PDA MILL STATUS                                                   #
##########################################################################################################################

# Get Input Params
data = json.loads(sys.argv[1])

# Check Received Data
cause = prevent_billet.cause(data=data, status='gap_off')
if not isinstance(cause, str) or cause == '':
    raise Exception('data not valid')

# Get Target JSON
fileDir = os.path.dirname(os.path.abspath(__file__))
pbPath = os.path.abspath(os.path.join(fileDir, './prevent_billet.json'))

# Write to JSON File
json.dump(data, open(pbPath, 'w'), indent=2)

##########################################################################################################################

    
