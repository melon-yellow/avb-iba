
##########################################################################################################################

# Imports
import sys
import json
import requests

##########################################################################################################################
#                                             UTILIZACAO - LAMINADOR & TREFILA                                           #
##########################################################################################################################

# Get Input Params
timestamp = json.loads(sys.argv[1])
params = json.loads(sys.argv[2])
thermo = json.loads(sys.argv[3])

# Request
requests.post(
    url = 'http://10.20.6.61:3000/pda_rod_therm_ntm',
    auth = ('iba.avb', 'efbuy3uy42ub429d'),
    json = {
        'action': 'pda_rod_therm_ntm',
        't': timestamp,
        'params': params,
        'therm': thermo
    }
)

##########################################################################################################################
