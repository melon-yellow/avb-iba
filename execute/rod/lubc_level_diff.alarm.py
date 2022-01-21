
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
time = str(argv[1])
delta = float(argv[2])

# Check Inputs
if not isinstance(time, str):
    raise Exception('key "time" not valid')
if not isinstance(delta, (int, float)):
    raise Exception('key "delta" not valid')

# Check Raise or Lower
mod = '-'
if delta > 0: mod = 'subiu'
if delta < 0: mod = 'caiu'

# Round Abs Delta
delta = abs(round(delta, 1))

# message
msg = ' '.join([
    f'*Atenção!* ⚠️ O nível da lub-C {mod}',
    f'{delta}% em {time}!'
])

# log
log = 'iba::pda_rod_lubc_level_diff'

# send message
avbot.sends(to='avb.laminacao.manutencao.g', text=msg, log=log)
avbot.sends(to='avb.laminacao.supervisao.g', text=msg, log=log)
avbot.sends(to='avb.automacao.anthony', text=msg, log=log)

##########################################################################################################################
