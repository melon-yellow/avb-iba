
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
#                                                      RHF HIGH TEMP ALARM                                               #
##########################################################################################################################

# Get Input Params
zn = str(argv[1])
valve = str(argv[2])
gs = str(argv[3])

# Check Inputs
if not isinstance(zn, str): raise Exception('key "N" not valid')
if not isinstance(valve, str): raise Exception('key "valve" not valid')
if not isinstance(gs, str): raise Exception('key "GA" not valid')

# Check Valve Letter
if len(valve) != 1: raise Exception('key "valve" not valid')

# Get Furnace Zone
zone = '-'
if zn == '101': zone = 'Pré Aquecimento'
elif zn == '102': zone = 'Aquecimento'
elif zn == '103': zone = 'Enxarque Superior'
elif zn == '104': zone = 'Enxarque Inferior'
else:
    raise Exception('key "N" not valid')

# Get Gas Type
gas = '-'
number = ['-', '-']
if gs == 'G':
    gas = 'Gás'
    number = ['1','3']
elif gs == 'A':
    gas = 'Ar'
    number = ['2','4']
else:
    raise Exception('key "GA" not valid')

# message
msg = ' '.join([
    '*Atenção!* ⚠️ A temperatura está alta na Linha de',
    f'{gas} ({valve}) da Zona de {zone} do forno!',
    f'(UV{zn}{number[0]}{valve}',
    f'/UV{zn}{number[1]}{valve})'
])

# log
log = 'iba::pda_rhf_high_temp_alarm'

# send message
avbot.sends(to='avb.laminacao.manutencao.g', text=msg, log=log)
avbot.sends(to='avb.laminacao.supervisao.g', text=msg, log=log)
avbot.sends(to='avb.automacao.anthony', text=msg, log=log)

##########################################################################################################################
