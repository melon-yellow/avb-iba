
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
#                                                 NTM CASQUILHOS TEMP ALARM                                              #
##########################################################################################################################

# Get Input Params
std = int(sys.argv[1])
_side = str(sys.argv[2])
manc = str(sys.argv[3])

# Check Inputs
if not isinstance(std, int):
    raise Exception('key "std" not valid')
if not isinstance(_side, str):
    raise Exception('key "side" not valid')
if not isinstance(manc, str):
    raise Exception('key "manc" not valid')

side = 'direito' if _side == 'R' else 'esquerdo'

# message
msg = ' '.join(('*Atenção!* ⚠️ A temperatura do mancal {} ({})',
    'da Gaiola {} chegou acima de 95 graus!')).format(side, manc, std)

# log
log = 'py_avbot_iba::pda_rod_ntm_casc_temp_alarm'

# send message
avbot.send('grupo_supervisores', msg, log)
avbot.send('grupo_automation', msg, log)
avbot.send('joao_paulo', msg, log)
avbot.send('anthony', msg, log)

##########################################################################################################################
