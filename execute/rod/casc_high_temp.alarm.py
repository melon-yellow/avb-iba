
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
#                                                 NTM CASQUILHOS TEMP ALARM                                              #
##########################################################################################################################

# Get Input Params
std = int(sys.argv[1])
sd = str(sys.argv[2])
manc = str(sys.argv[3])

# Check Inputs
if not isinstance(std, int): raise Exception('key "std" not valid')
if not isinstance(sd, str): raise Exception('key "side" not valid')
if not isinstance(manc, str): raise Exception('key "manc" not valid')

# Get Casc-Side
side = '-'
if sd == 'R': side = 'direito'
if sd == 'L': side = 'esquerdo'

# message
msg = ' '.join([
    f'*Atenção!* ⚠️ A temperatura do mancal {side} ({manc})',
    f'da Gaiola {std} chegou acima de 95° C !'
])

# log
log = 'iba::pda_rod_ntm_casc_temp_alarm'

# send message
avbot.sends(to='laminador_mantenedores', text=msg, log=log)
avbot.sends(to='grupo_supervisores', text=msg, log=log)
avbot.sends(to='grupo_automation', text=msg, log=log)
avbot.sends(to='anthony', text=msg, log=log)

##########################################################################################################################
