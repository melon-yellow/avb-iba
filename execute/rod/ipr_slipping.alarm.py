
##########################################################################################################################

# Imports
import os
import sys
import json
from py_wapp import Wapp

##########################################################################################################################

# Get Target JSON
fileDir = os.path.dirname(os.path.abspath(__file__))
tarPath = os.path.abspath(os.path.join(fileDir, '../../whatsapp/target.json'))
target = json.load(open(tarPath, 'r'))

# Instance Whatsapp
avbot = Wapp(target)

##########################################################################################################################
#                                                       IPR SLIP ALARM                                                   #
##########################################################################################################################

# Get Input Params
ipr = int(sys.argv[1])

# Check Inputs
if not isinstance(ipr, int):
    raise Exception('key "ipr" not valid')

# message
msg = '*Atenção!* ⚠️ O pinch roll 0{} está patinando!'.format(ipr)

# log
log = 'py_avbot_iba::pda_rod_ipr_slip_alarm'

# send message
avbot.send('grupo_supervisores', msg, log)
avbot.send('grupo_automation', msg, log)
avbot.send('joao_paulo', msg, log)
avbot.send('anthony', msg, log)

##########################################################################################################################
