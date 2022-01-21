
##########################################################################################################################

# Imports
from os import getenv
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

# message
msg = '*Atenção!* ⚠️ (avbot is running)'

# log
log = 'iba::test'

# send message
res = avbot.sends(to='avb.automacao.anthony', text=msg, log=log)
print(res)

##########################################################################################################################
