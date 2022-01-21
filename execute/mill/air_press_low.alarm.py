
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
#                                                  MILL AIR PRESS LOW ALARM                                              #
##########################################################################################################################

# Get Input Params
press = float(argv[1])

# On Alarm
if not isinstance(press, (int, float)):
    raise Exception('key "press" not valid')

# message
msg = ' '.join([
    '*Atenção!* ⚠️ A pressão de Ar Comprimido',
    f'do Laminador chegou abaixo de {press} Bar!'
])

# log
log = 'iba::pda_mill_air_press_low'

# send message
avbot.sends(to='avb.laminacao.manutencao.g', text=msg, log=log)
avbot.sends(to='avb.laminacao.supervisao.g', text=msg, log=log)
avbot.sends(to='avb.automacao.anthony', text=msg, log=log)

##########################################################################################################################
