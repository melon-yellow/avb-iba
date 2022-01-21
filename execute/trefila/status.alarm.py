
##########################################################################################################################

# Imports
from os import getenv
from sys import argv
from json import loads
from dotenv import load_dotenv
from requests import post
from py_wapp.wapp import Wapp

##########################################################################################################################

# Get Enviromental Variables
load_dotenv()

# Instance Whatsapp
avbot = Wapp({
    'address': getenv('WHATSAPP_TARGET_ADDRESS'),
    'user': getenv('WHATSAPP_TARGET_USER'),
    'password': getenv('WHATSAPP_TARGET_PASSWORD')
})

##########################################################################################################################
#                                                   TRF STATUS ALARM                                                     #
##########################################################################################################################

# Get Input Params
mq = loads(argv[1])
status = loads(argv[2])

# Options Dictionary
switcher = dict(
    stop = '😔 Máquina {} parada!‍',
    start = '😁 Máquina {} ligada!'
)

if status not in switcher:
    raise Exception("invalid status")

log = f'bot::pda_trf_status({mq}, {status})'
msg = switcher[status].format(mq)

avbot.sends(to='avb.trefila.jayron', text=msg, log=log)
avbot.sends(to='avb.automacao.anthony', text=msg, log=log)

##########################################################################################################################

# Request
post(
    url = getenv('WHATSAPP_TARGET_GUSAL2_ADDRESS'),
    auth = (
        getenv('WHATSAPP_TARGET_GUSAL2_USER'),
        getenv('WHATSAPP_TARGET_GUSAL2_PASSWORD')
    ),
    json = {
        'action': 'pda_trf_status',
        'mq': mq,
        'status': status
    }
)

##########################################################################################################################
