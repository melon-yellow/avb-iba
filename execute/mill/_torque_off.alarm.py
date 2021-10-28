
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
#                                                      TORQUE ALARME                                                     #
##########################################################################################################################

# Get Input Params
t = json.loads(sys.argv[1])
std = int(sys.argv[2])

# Check Inputs
if not isinstance(std, int):
    raise Exception('key "std" not valid')

# message
msg = '*Atenção!* ⚠️ O Torque da gaiola {} está anormal!'.format(std)

# log
log = 'py_avbot_iba::pda_mill_m_off({})'.format(std)

# send message
avbot.send('anthony', msg, log)

##########################################################################################################################
