
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
    'addr': os.getenv('WHATSAPP_TARGET_ADDR'),
    'auth':{
        'user': os.getenv('WHATSAPP_TARGET_USER'),
        'password': os.getenv('WHATSAPP_TARGET_PASSWORD')
    }
})

##########################################################################################################################
#                                                    FISHLINE FLICK ALARM                                                #
##########################################################################################################################

# Get Input Params
_fl = int(sys.argv[1])

# On Alarm
if not isinstance(_fl, int):
    raise Exception('key "fl" not valid')

# Select Fishline
fl = 'principal' if _fl else 'da Breakout Box'

# message
msg = f'*Atenção!* ⚠️ O Fishline {fl} piscou!'

# log
log = 'iba::pda_rod_fishline_flick_alarm'

# send message
avbot.send(to='grupo_supervisores', text=msg, log=log)
avbot.send(to='grupo_automation', text=msg, log=log)
avbot.send(to='anthony', text=msg, log=log)

##########################################################################################################################
