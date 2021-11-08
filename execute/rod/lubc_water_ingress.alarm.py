
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
    'address': os.getenv('WHATSAPP_TARGET_ADDRESS'),
    'user': os.getenv('WHATSAPP_TARGET_USER'),
    'password': os.getenv('WHATSAPP_TARGET_PASSWORD')
})

##########################################################################################################################
#                                                   LUB-C HIGH TEMP ALARM                                                #
##########################################################################################################################

# Get Input Params
aw = int(sys.argv[1])

# Check Inputs
if not isinstance(aw, int):
    raise Exception('key "aw" not valid')

# message
msg = ' '.join([
    '*Atenção!* ⚠️ A umidade relativa do óleo',
    f'da lub-C chegou acima de {aw}% !'
])

# log
log = 'iba::pda_rod_lubc_water_ingress'

# send message
avbot.sends(to='laminador_mantenedores', text=msg, log=log)
avbot.sends(to='grupo_supervisores', text=msg, log=log)
avbot.sends(to='grupo_automation', text=msg, log=log)
avbot.sends(to='anthony', text=msg, log=log)

##########################################################################################################################
