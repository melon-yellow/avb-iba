
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
#                                                       IPR SLIP ALARM                                                   #
##########################################################################################################################

# Get Input Params
ipr = int(sys.argv[1])

# Check Inputs
if not isinstance(ipr, int):
    raise Exception('key "ipr" not valid')

# message
msg = f'*Atenção!* ⚠️ O pinch roll 0{ipr} está patinando!'

# log
log = 'iba::pda_rod_ipr_slip_alarm'

# send message
avbot.sends(to='grupo_supervisores', text=msg, log=log)
avbot.sends(to='grupo_automation', text=msg, log=log)
avbot.sends(to='anthony', text=msg, log=log)

##########################################################################################################################
