
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
#                                                    NTM VIBRATION REPORT                                                #
##########################################################################################################################

# Get Input Params
timestamp = loads(argv[1])
params = loads(argv[2])
rpm = float(argv[3])
vib = float(argv[4])

# Request
post(
    url = getenv('AVB_IBA_NTM_VIB_REPORT_ADDRESS'),
    auth = (
        getenv('AVB_IBA_NTM_VIB_REPORT_USER'),
        getenv('AVB_IBA_NTM_VIB_REPORT_PASSWORD')
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
