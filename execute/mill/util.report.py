
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
#                                             UTILIZACAO - LAMINADOR & TREFILA                                           #
##########################################################################################################################

# Get Input Params
timestamp = json.loads(sys.argv[1])
mill = json.loads(sys.argv[2])
trf = json.loads(sys.argv[3])

# Request
requests.post(
    url = os.getenv('AVB_IBA_UTIL_REPORT_ADDR'),
    auth = (
        os.getenv('AVB_IBA_UTIL_REPORT_USER'),
        os.getenv('AVB_IBA_UTIL_REPORT_PASSWORD')
    ),
    json = {
        'action': 'pda_util',
        't': timestamp,
        'mill': mill,
        'trf': trf
    }
)

##########################################################################################################################
