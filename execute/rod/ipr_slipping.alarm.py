
##########################################################################################################################

# Imports
from os import getenv
from sys import argv
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
#                                                       IPR SLIP ALARM                                                   #
##########################################################################################################################

# Get Input Params
ipr = int(argv[1])

# Check Inputs
if not isinstance(ipr, int):
    raise Exception('key "ipr" not valid')

# message
msg = f'*Atenção!* ⚠️ O pinch roll 0{ipr} está patinando!'

# log
log = 'iba::pda_rod_ipr_slip_alarm'

# send message
avbot.sends(to='avb.laminacao.supervisao.g', text=msg, log=log)
avbot.sends(to='avb.automacao.anthony', text=msg, log=log)

##########################################################################################################################
