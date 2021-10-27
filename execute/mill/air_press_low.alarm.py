
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
#                                                  MILL AIR PRESS LOW ALARM                                              #
##########################################################################################################################

# Get Input Params
press = float(sys.argv[1])

# On Alarm
if not isinstance(press, int) or not isinstance(press, float):
    raise Exception('key "press" not valid')

# message
msg = ' '.join(('*Atenção!* ⚠️ A pressão de Ar Comprimido',
    'do Laminador chegou abaixo de {} Bar!')).format(press)

# log
log = 'py_avbot_iba::pda_mill_air_press_low'

# send message
avbot.send('anthony', msg, log)
avbot.send('laminador_mantenedores', msg, log)
avbot.send('joao_paulo', msg, log)

##########################################################################################################################
