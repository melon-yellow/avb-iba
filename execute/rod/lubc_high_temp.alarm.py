
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
temp = int(sys.argv[1])

# Check Inputs
if not isinstance(temp, int):
    raise Exception('key "temp" not valid')

# message
msg = ' '.join(('*Atenção!* ⚠️ A temperatura do óleo da',
    'lub-C chegou acima de {} graus!')).format(temp)

# log
log = 'iba::pda_rod_lubc_high_temp_alarm'

# send message
avbot.send('grupo_supervisores', msg, log)
avbot.send('grupo_automation', msg, log)
avbot.send('joao_paulo', msg, log)
avbot.send('anthony', msg, log)

##########################################################################################################################
