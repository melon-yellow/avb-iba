
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
#                                                 NTM CASQUILHOS TEMP ALARM                                              #
##########################################################################################################################

# Get Input Params
std = int(sys.argv[1])
_side = str(sys.argv[2])
manc = str(sys.argv[3])

# Check Inputs
if not isinstance(std, int): raise Exception('key "std" not valid')
if not isinstance(_side, str): raise Exception('key "side" not valid')
if not isinstance(manc, str): raise Exception('key "manc" not valid')

# Get C-Side
side = '-'
if _side == 'R': side = 'direito'
if _side == 'E': side = 'esquerdo'

# message
msg = ' '.join(
    (f'*Atenção!* ⚠️ A temperatura do mancal {side} ({manc})',
    f'da Gaiola {std} chegou acima de 95 graus!')
)

# log
log = 'iba::pda_rod_ntm_casc_temp_alarm'

# send message
avbot.send(to='grupo_supervisores', text=msg, log=log)
avbot.send(to='grupo_automation', text=msg, log=log)
avbot.send(to='joao_paulo', text=msg, log=log)
avbot.send(to='anthony', text=msg, log=log)

##########################################################################################################################
