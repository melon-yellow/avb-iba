
##########################################################################################################################

# Imports
import os
import sys
import json
from py_wapp import Wapp

# Modules
import prevent_billet

##########################################################################################################################

# Get Target JSON
fileDir = os.path.dirname(os.path.abspath(__file__))
pbPath = os.path.abspath(os.path.join(fileDir, './prevent_billet.json'))
tarPath = os.path.abspath(os.path.join(fileDir, '../../../whatsapp/target.json'))
target = json.load(open(tarPath, 'r'))

# Instance Whatsapp
avbot = Wapp(target)

##########################################################################################################################
#                                                      PDA MILL STATUS                                                   #
##########################################################################################################################

# Get Input Params
status = str(sys.argv[1])
data = json.loads(sys.argv[2])

# Check Inputs
if not isinstance(status, str):
    raise Exception('key "status" not found')
if not isinstance(data, dict):
    raise Exception('key "data" not found')

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
    raise Exception('status not valid')

# Get Message Text
log = 'py_avbot_iba::pda_mill_status({})'.format(status)
msg = switcher[status]

# Gap-Off First Fault
if status == 'gap_off':
    # Read from JSON File
    data = json.load(open(pbPath, 'r'))

# Get Cause
if status == 'cobble' or status == 'gap_off':
    cause = prevent_billet.cause(data, status)
    if isinstance(cause, str) and cause != '':
        msg = (msg + '\n' + '_Motivo: ' + cause + '_')

# Send only Start/Stop Messages
if status != 'exit_fur':
    avbot.send('gerencia_laminacao', msg, log)

# Send Messages
avbot.send('grupo_supervisores', msg, log)
avbot.send('anthony', msg, log)

##########################################################################################################################

    
