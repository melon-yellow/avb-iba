
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
#                                                   LUB-C HIGH TEMP ALARM                                                #
##########################################################################################################################

# Get Input Params
temp = int(argv[1])

# Check Inputs
if not isinstance(temp, int):
    raise Exception('key "temp" not valid')

# message
msg = ' '.join([
    '*Atenção!* ⚠️ A temperatura do óleo da',
    f'lub-C chegou acima de {temp}° C !'
])

# log
log = 'iba::pda_rod_lubc_high_temp_alarm'

# send message
avbot.sends(to='avb.laminacao.manutencao.g', text=msg, log=log)
avbot.sends(to='avb.laminacao.supervisao.g', text=msg, log=log)
avbot.sends(to='avb.automacao.anthony', text=msg, log=log)

##########################################################################################################################
