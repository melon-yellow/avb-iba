
##########################################################################################################################

# Imports
import os
import sys
import dotenv
from py_wapp import Wapp

##########################################################################################################################

# Get Enviromental Variables
dotenv.load_dotenv()

# Instance Whatsapp
avbot = Wapp({
    'address': os.getenv('WHATSAPP_TARGET_ADDRESS'),
    'user': os.getenv('WHATSAPP_TARGET_USER'),
    'password': os.getenv('WHATSAPP_TARGET_PASSWORD')
})

##########################################################################################################################
#                                                   LUB-C HIGH TEMP ALARM                                                #
##########################################################################################################################

# Get Input Params
time = str(sys.argv[1])
delta = float(sys.argv[2])

# Check Inputs
if not isinstance(time, str):
    raise Exception('key "time" not valid')
if not isinstance(delta, (int, float)):
    raise Exception('key "delta" not valid')

# Check Raise or Lower
mod = '-'
if delta > 0: mod = 'subiu'
if delta < 0: mod = 'caiu'

# Round Abs Delta
delta = abs(round(delta, 1))

# message
msg = ' '.join([
    f'*Atenção!* ⚠️ O nível da lub-C {mod}',
    f'{delta}% em {time}!'
])

# log
log = 'iba::pda_rod_lubc_level_diff'

# send message
avbot.sends(to='laminador_mantenedores', text=msg, log=log)
avbot.sends(to='grupo_supervisores', text=msg, log=log)
avbot.sends(to='grupo_automation', text=msg, log=log)
avbot.sends(to='anthony', text=msg, log=log)

##########################################################################################################################
