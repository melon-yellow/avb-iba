
raise Exception('disabled')

##########################################################################################################################

# Imports
from os import getenv
from sys import argv
from json import loads
from dotenv import load_dotenv
from py_wapp.wapp import Wapp

##########################################################################################################################

# Get Enviromental Variables
load_dotenv()

# Instance Whatsapp
avbot = Wapp({
    'address': getenv('WHATSAPP_TARGET_ADDRESS'),
    'user': getenv('WHATSAPP_TARGET_USER'),
    'password': getenv('WHATSAPP_TARGET_PASSWORD')
})

##########################################################################################################################
#                                                      TORQUE ALARME                                                     #
##########################################################################################################################

# Get Input Params
t = loads(argv[1])
std = int(argv[2])

# Check Inputs
if not isinstance(std, (int, float)):
    raise Exception('key "std" not valid')

# message
msg = f'*Atenção!* ⚠️ O Torque da gaiola {std} está anormal!'

# log
log = f'iba::pda_mill_m_off({std})'

# send message
avbot.sends(to='avb.automacao.anthony', text=msg, log=log)

##########################################################################################################################
