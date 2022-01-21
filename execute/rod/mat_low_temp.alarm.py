
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
#                                                     ROD LOW TEMP ALARM                                                 #
##########################################################################################################################

# Get Input Params
temp = int(argv[1])

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
avbot.sends(to='avb.laminacao.supervisao.g', text=msg, log=log)
avbot.sends(to='avb.automacao.anthony', text=msg, log=log)

##########################################################################################################################
