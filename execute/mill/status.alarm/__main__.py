
##########################################################################################################################

# Imports
from os import getenv, path
from sys import argv
from json import loads, load
from dotenv import load_dotenv
from py_wapp.wapp import Wapp

# Modules
from prevent_billet import cause

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
#                                                      PDA MILL STATUS                                                   #
##########################################################################################################################

# Get Input Params
status = str(argv[1])
data = loads(argv[2])

# Check Inputs
if not isinstance(status, str):
    raise Exception('invalid argument "status"')
if not isinstance(data, dict):
    raise Exception('invalid argument "data"')

# Options Dictionary
switcher = dict(
    ghost = 'Passando barra fantasma! 👻',
    exit_fur = 'Peça saindo do forno! 🔥',
    start = 'Laminador produzindo! 🙏',
    stop = 'Laminador parado! 🤷‍♂️💸‍',
    gap = 'Laminador no GAP‍! 🙏💰',
    gap_off = 'O GAP foi desligado! 🤷‍♂️🐢',
    cobble = 'Sucata no laminador! 🤦💸💸‍'
)

# Check Status Key
if status not in switcher:
    raise Exception('invalid argument "status"')

# Get Message Text
log = f'iba::pda_mill_status({status})'
msg = switcher[status]

# Gap-Off First Fault
if status == 'gap_off':
    fileDir = path.dirname(path.abspath(__file__))
    pbPath = path.abspath(path.join(fileDir, './prevent_billet.json'))
    data = load(open(pbPath, 'r'))

# Get Cause
if status == 'cobble' or status == 'gap_off':
    cause = cause(data=data, status=status)
    if isinstance(cause, str) and cause != '':
        msg = f'{msg}\n_Motivo: {cause}_'

# Send only Start/Stop Messages
if status != 'exit_fur':
    avbot.sends(to='avb.laminacao.gerencia.g', text=msg, log=log)

# Send Messages
avbot.sends(to='avb.laminacao.supervisao.g', text=msg, log=log)
avbot.sends(to='avb.automacao.anthony', text=msg, log=log)

##########################################################################################################################

    
