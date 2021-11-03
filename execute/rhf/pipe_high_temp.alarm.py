
##########################################################################################################################

# Imports
import os
import sys
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
#                                                      RHF HIGH TEMP ALARM                                               #
##########################################################################################################################

# Get Input Params
_zone = str(sys.argv[1])
valve = str(sys.argv[2])
_gas = str(sys.argv[3])

# Check Inputs
if not isinstance(_zone, str): raise Exception('key "N" not valid')
if not isinstance(valve, str): raise Exception('key "valve" not valid')
if not isinstance(_gas, str): raise Exception('key "GA" not valid')

# Check Valve Letter
if len(valve) != 1: raise Exception('key "valve" not valid')

# Get Furnace Zone
zone = ''
if _zone == '101': zone = 'Pré Aquecimento'
elif _zone == '102': zone = 'Aquecimento'
elif _zone == '103': zone = 'Enxarque Superior'
elif _zone == '104': zone = 'Enxarque Inferior'
else:
    raise Exception('key "N" not valid')

# Get Gas Type
gas = ''
nv = ['', '']
if _gas == 'G':
    gas = 'Gás'
    nv = ['1','3']
elif _gas == 'A':
    gas = 'Ar'
    nv = ['2','4']
else:
    raise Exception('key "GA" not valid')

# message
msg = ' '.join(
    ('*Atenção!* ⚠️ A temperatura está alta na Linha de',
    f'{gas} ({valve}) da Zona de {zone} do forno!',
    f'(UV{_zone}{nv[0]}{valve}/UV{_zone}{nv[1]}{valve})')
)
        
# log
log = 'iba::pda_rhf_high_temp_alarm'

# send message
avbot.send(to='laminador_mantenedores', text=msg, log=log)
avbot.send(to='grupo_supervisores', text=msg, log=log)
avbot.send(to='joao_paulo', text=msg, log=log)
avbot.send(to='anthony', text=msg, log=log)

##########################################################################################################################
