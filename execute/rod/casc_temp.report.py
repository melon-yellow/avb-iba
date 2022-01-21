
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
#                                                NTM THERMOCOUPLES REPORT                                                #
##########################################################################################################################

# Get Input Params
timestamp = loads(argv[1])
params = loads(argv[2])
thermo = loads(argv[3])

# Request
post(
    url = getenv('AVB_IBA_NTM_TEMP_REPORT_ADDRESS'),
    auth = (
        getenv('AVB_IBA_NTM_TEMP_REPORT_USER'),
        getenv('AVB_IBA_NTM_TEMP_REPORT_PASSWORD')
    ),
    json = {
        'action': 'pda_rod_therm_ntm',
        't': timestamp,
        'params': params,
        'therm': thermo
    }
)

##########################################################################################################################
