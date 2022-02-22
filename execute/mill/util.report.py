
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
#                                             UTILIZACAO - LAMINADOR & TREFILA                                           #
##########################################################################################################################

# Get Input Params
timestamp = loads(argv[1])
mill = loads(argv[2])
trf = loads(argv[3])

# Request
post(
    url = getenv('AVB_IBA_UTIL_REPORT_ADDRESS'),
    auth = (
        getenv('AVB_IBA_UTIL_REPORT_USER'),
        getenv('AVB_IBA_UTIL_REPORT_PASSWORD')
    ),
    json = {
        'action': 'pda_util',
        't': timestamp,
        'mill': mill,
        'trf': trf
    }
)

##########################################################################################################################
