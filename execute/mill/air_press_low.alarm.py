
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
#                                                  MILL AIR PRESS LOW ALARM                                              #
##########################################################################################################################

# Get Input Params
press = float(sys.argv[1])

# On Alarm
if not isinstance(press, (int, float)):
    raise Exception('key "press" not valid')

# message
msg = ' '.join([
    '*Atenção!* ⚠️ A pressão de Ar Comprimido',
    f'do Laminador chegou abaixo de {press} Bar!'
])

# log
log = 'iba::pda_mill_air_press_low'

# send message
avbot.sends(to='laminador_mantenedores', text=msg, log=log)
avbot.sends(to='grupo_supervisores', text=msg, log=log)
avbot.sends(to='anthony', text=msg, log=log)

##########################################################################################################################
