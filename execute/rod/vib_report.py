
##########################################################################################################################

# Imports
import sys
import json
import requests

##########################################################################################################################
#                                                    NTM VIBRATION REPORT                                                #
##########################################################################################################################

# Get Input Params
timestamp = json.loads(sys.argv[1])
params = json.loads(sys.argv[2])
rpm = float(sys.argv[3])
vib = float(sys.argv[4])

# Request
requests.post(
    url = 'http://10.20.6.61:3000/pda_rod_vib_ntm',
    auth = ('iba.avb', 'efbuy3uy42ub429d'),
    json = {
        'action': 'pda_rod_vib_ntm',
        't': timestamp,
        'params': params,
        'rpm': rpm,
        'vib': vib
    }
)

##########################################################################################################################
