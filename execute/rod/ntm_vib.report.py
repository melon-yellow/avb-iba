
##########################################################################################################################

# Imports
import os
import sys
import json
import requests
import dotenv

##########################################################################################################################

# Get Enviromental Variables
dotenv.load_dotenv()

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
    url = os.getenv('AVB_IBA_NTM_VIB_REPORT_ADDR'),
    auth = (
        os.getenv('AVB_IBA_NTM_VIB_REPORT_USER'),
        os.getenv('AVB_IBA_NTM_VIB_REPORT_PASSWORD')
    ),
    json = {
        'action': 'pda_rod_vib_ntm',
        't': timestamp,
        'params': params,
        'rpm': rpm,
        'vib': vib
    }
)

##########################################################################################################################
