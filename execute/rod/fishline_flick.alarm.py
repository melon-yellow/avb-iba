
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
#                                                    FISHLINE FLICK ALARM                                                #
##########################################################################################################################

# Get Input Params
_fl = int(sys.argv[1])

# On Alarm
if not isinstance(_fl, int):
    raise Exception('key "fl" not valid')

# Select Fishline
fl = ('principal' if _fl != 0 else 'da Breakout Box')

# message
msg = '*Atenção!* ⚠️ O Fishline {} piscou!'.format(fl)

# log
log = 'py_avbot_iba::pda_rod_fishline_flick_alarm'

# send message
avbot.send('grupo_supervisores', msg, log)
avbot.send('grupo_automation', msg, log)
avbot.send('joao_paulo', msg, log)
avbot.send('anthony', msg, log)

##########################################################################################################################
