
##########################################################################################################################

# Imports
import os
import sys
import json
import dotenv
import requests
from py_wapp import Wapp

##########################################################################################################################

# Get Enviromental Variables
dotenv.load_dotenv()

# Instance Whatsapp
avbot = Wapp({
    'address': os.getenv('WHATSAPP_TARGET_ADDRESS'),
    'user': os.getenv('WHATSAPP_TARGET_USER'),
    'password': os.getenv('WHATSAPP_TARGET_PASSWORD')
})

##########################################################################################################################
#                                                   TRF STATUS ALARM                                                     #
##########################################################################################################################

# Get Input Params
mq = json.loads(sys.argv[1])
status = json.loads(sys.argv[2])

# Options Dictionary
switcher = dict(
    stop = '😔 Máquina {} parada!‍',
    start = '😁 Máquina {} ligada!'
)

if status not in switcher:
    raise Exception("invalid status")

log = f'bot::pda_trf_status({mq}, {status})'
msg = switcher[status].format(mq)

avbot.send(to='avb.trefila.jayron', text=msg, log=log)
avbot.send(to='avb.automacao.anthony', text=msg, log=log)

# Request
requests.post(
    url = os.getenv('WHATSAPP_TARGET_GUSAL2_ADDRESS'),
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
