
##########################################################################################################################

# Imports
import os
import sys
import json
import requests

##########################################################################################################################

# Get Target JSON
fileDir = os.path.dirname(os.path.abspath(__file__))
tarPath = os.path.abspath(os.path.join(fileDir, '../../whatsapp/target.gusal2.json'))
target = json.load(open(tarPath, 'r'))

##########################################################################################################################
#                                                   LUB-C HIGH TEMP ALARM                                                #
##########################################################################################################################

# Get Input Params
timestamp = json.loads(sys.argv[1])
util = json.loads(sys.argv[2])

# Request
requests.post(
    url = target['addr'],
    auth = (
        target['auth']['user'],
        target['auth']['password']
    ),
    json = {
        'action': 'pda_trf_report',
        't': timestamp,
        'util': util
    }
)

##########################################################################################################################
