
##########################################################################################################################

# Imports
import os
import json
from py_wapp import Wapp

##########################################################################################################################

# Get Target JSON
fileDir = os.path.dirname(os.path.abspath(__file__))
tarPath = os.path.abspath(os.path.join(fileDir, './target.json'))
target = json.load(open(tarPath, 'r'))

# Instance Whatsapp
wapp = Wapp(target)

##########################################################################################################################

# send message
wapp.send('anthony', 'test message', 'testing')

##########################################################################################################################
