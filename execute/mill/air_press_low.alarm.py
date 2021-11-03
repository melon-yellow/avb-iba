
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
#                                                  MILL AIR PRESS LOW ALARM                                              #
##########################################################################################################################

# Get Input Params
press = float(sys.argv[1])

# On Alarm
if not isinstance(press, (int, float)):
    raise Exception('key "press" not valid')

# message
msg = ' '.join(
    ('*Atenção!* ⚠️ A pressão de Ar Comprimido',
    f'do Laminador chegou abaixo de {press} Bar!')
)

# log
log = 'iba::pda_mill_air_press_low'

# send message
avbot.send(to='laminador_mantenedores', text=msg, log=log)
avbot.send(to='joao_paulo', text=msg, log=log)
avbot.send(to='anthony', text=msg, log=log)

##########################################################################################################################
