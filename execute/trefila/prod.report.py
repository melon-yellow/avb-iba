
##########################################################################################################################

# Imports
from os import getenv
from sys import argv
from json import loads
from dotenv import load_dotenv
from requests import post

##########################################################################################################################

# Get Enviromental Variables
load_dotenv()

##########################################################################################################################
#                                                   LUB-C HIGH TEMP ALARM                                                #
##########################################################################################################################

# Get Input Params
timestamp = loads(argv[1])
util = loads(argv[2])

# Request
post(
    url = getenv('WHATSAPP_TARGET_GUSAL2_ADDRESS'),
    auth = (
        getenv('WHATSAPP_TARGET_GUSAL2_USER'),
        getenv('WHATSAPP_TARGET_GUSAL2_PASSWORD')
    ),
    json = {
        'action': 'pda_trf_report',
        't': timestamp,
        'util': util
    }
)

##########################################################################################################################
