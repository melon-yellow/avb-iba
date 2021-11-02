
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
mq = json.loads(sys.argv[1])
status = json.loads(sys.argv[2])

# Request
requests.post(
    url = os.getenv('WHATSAPP_TARGET_GUSAL2_ADDR'),
    auth = (
        os.getenv('WHATSAPP_TARGET_GUSAL2_USER'),
        os.getenv('WHATSAPP_TARGET_GUSAL2_PASSWORD')
    ),
    json = {
        'action': 'pda_trf_status',
        'mq': mq,
        'status': status
    }
)

##########################################################################################################################
