
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
#                                                     ROD LOW TEMP ALARM                                                 #
##########################################################################################################################

# Get Input Params
temp = int(sys.argv[1])

# Check Inputs
if not isinstance(temp, int):
    raise Exception('key "temp" not valid')

# message
msg = ' '.join([
    '*Atenção!* ⚠️ A temperatura na entrada',
    f'do bloco chegou abaixo de {temp}° C !'
])

# log
log = 'iba::pda_rod_low_temp_alarm'

# send message
avbot.sends(to='grupo_supervisores', text=msg, log=log)
avbot.sends(to='grupo_automation', text=msg, log=log)
avbot.sends(to='anthony', text=msg, log=log)

##########################################################################################################################
