
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
#                                                    FISHLINE FLICK ALARM                                                #
##########################################################################################################################

# Get Input Params
index = int(sys.argv[1])

# On Alarm
if not isinstance(index, int):
    raise Exception('key "index" not valid')

# Select Fishline
fl = '-'
if index == 1: fl = 'do bloco'
if index == 0: fl = 'da Breakout Box'

# message
msg = f'*Atenção!* ⚠️ O Fishline {fl} piscou!'

# log
log = 'iba::pda_rod_fishline_flick_alarm'

# send message
avbot.sends(to='laminador_mantenedores', text=msg, log=log)
avbot.sends(to='grupo_supervisores', text=msg, log=log)
avbot.sends(to='grupo_automation', text=msg, log=log)
avbot.sends(to='anthony', text=msg, log=log)

##########################################################################################################################
