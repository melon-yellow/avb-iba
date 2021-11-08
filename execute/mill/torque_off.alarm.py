
raise Exception('disabled')

##########################################################################################################################

# Imports
import os
import sys
import json
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
#                                                      TORQUE ALARME                                                     #
##########################################################################################################################

# Get Input Params
t = json.loads(sys.argv[1])
std = int(sys.argv[2])

# Check Inputs
if not isinstance(std, (int, float)):
    raise Exception('key "std" not valid')

# message
msg = f'*Atenção!* ⚠️ O Torque da gaiola {std} está anormal!'

# log
log = f'iba::pda_mill_m_off({std})'

# send message
avbot.sends(to='anthony', text=msg, log=log)

##########################################################################################################################
