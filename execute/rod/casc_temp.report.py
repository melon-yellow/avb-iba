
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
#                                                NTM THERMOCOUPLES REPORT                                                #
##########################################################################################################################

# Get Input Params
timestamp = json.loads(sys.argv[1])
params = json.loads(sys.argv[2])
thermo = json.loads(sys.argv[3])

# Request
requests.post(
    url = os.getenv('AVB_IBA_NTM_TEMP_REPORT_ADDRESS'),
    auth = (
        os.getenv('AVB_IBA_NTM_TEMP_REPORT_USER'),
        os.getenv('AVB_IBA_NTM_TEMP_REPORT_PASSWORD')
    ),
    json = {
        'action': 'pda_rod_therm_ntm',
        't': timestamp,
        'params': params,
        'therm': thermo
    }
)

##########################################################################################################################
