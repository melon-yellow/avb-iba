
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
#                                                   LUB-C HIGH TEMP ALARM                                                #
##########################################################################################################################

# Get Input Params
aw = str(sys.argv[1])

# Check Inputs
if not isinstance(aw, str):
    raise Exception('key "aw" not valid')

ingress = ''
if aw == 'A': ingress = '0.7'
if aw == 'W': ingress = '0.9'

# message
msg = ' '.join(
    ('*Atenção!* ⚠️ A presença de água no óleo da',
    f'lub-C chegou acima de {ingress}% !')
)

# log
log = 'iba::pda_rod_lubc_water_ingress'

# send message
avbot.send(to='grupo_supervisores', text=msg, log=log)
avbot.send(to='grupo_automation', text=msg, log=log)
avbot.send(to='anthony', text=msg, log=log)

##########################################################################################################################
