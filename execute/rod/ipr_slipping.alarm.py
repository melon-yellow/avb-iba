
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
avbot.send(to='grupo_supervisores', text=msg, log=log)
avbot.send(to='grupo_automation', text=msg, log=log)
avbot.send(to='joao_paulo', text=msg, log=log)
avbot.send(to='anthony', text=msg, log=log)

##########################################################################################################################
