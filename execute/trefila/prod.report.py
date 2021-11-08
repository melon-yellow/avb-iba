
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
#                                                   LUB-C HIGH TEMP ALARM                                                #
##########################################################################################################################

# Get Input Params
timestamp = json.loads(sys.argv[1])
util = json.loads(sys.argv[2])

# Request
requests.post(
    url = os.getenv('WHATSAPP_TARGET_GUSAL2_ADDRESS'),
    auth = (
        os.getenv('WHATSAPP_TARGET_GUSAL2_USER'),
        os.getenv('WHATSAPP_TARGET_GUSAL2_PASSWORD')
    ),
    json = {
        'action': 'pda_trf_report',
        't': timestamp,
        'util': util
    }
)

##########################################################################################################################
