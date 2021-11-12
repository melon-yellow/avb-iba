
##########################################################################################################################

# Imports
import os
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

# message
msg = '*Atenção!* ⚠️ (avbot is running)'

# log
log = 'iba::test'

# send message
res = avbot.sends(to='anthony', text=msg, log=log)
print(res)

##########################################################################################################################
