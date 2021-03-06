
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
#                                                 NTM CASQUILHOS TEMP ALARM                                              #
##########################################################################################################################

# Get Input Params
std = int(argv[1])
sd = str(argv[2])
manc = str(argv[3])

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
avbot.sends(to='avb.laminacao.manutencao.g', text=msg, log=log)
avbot.sends(to='avb.laminacao.supervisao.g', text=msg, log=log)
avbot.sends(to='avb.laminacao.oficina.g', text=msg, log=log)
avbot.sends(to='avb.automacao.anthony', text=msg, log=log)

##########################################################################################################################
