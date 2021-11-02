
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
    'addr': os.getenv('WHATSAPP_TARGET_ADDR'),
    'auth':{
        'user': os.getenv('WHATSAPP_TARGET_USER'),
        'password': os.getenv('WHATSAPP_TARGET_PASSWORD')
    }
})

##########################################################################################################################
#                                                      TORQUE ALARME                                                     #
##########################################################################################################################

# Get Input Params
t = json.loads(sys.argv[1])
std = int(sys.argv[2])

# Check Inputs
if not isinstance(std, int):
    raise Exception('key "std" not valid')

# message
msg = '*Atenção!* ⚠️ O Torque da gaiola {} está anormal!'.format(std)

# log
log = 'iba::pda_mill_m_off({})'.format(std)

# send message
avbot.send('anthony', msg, log)

##########################################################################################################################
