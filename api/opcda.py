
#################################################################################################################################################

# Imports
import py_misc
import OpenOPC
import sys

#################################################################################################################################################

# Instance PyPDA
pypda = pyopc.PyOPC(misc).server('iba.ibaPdaOPC.1')

#################################################################################################################################################

# Declare Api
api = misc.api().host('0.0.0.0').port(3000)

#################################################################################################################################################

# PDA Endnode
@api.add('/api/pda/', methods=['POST'])
def py_pda(req):
    # Check for input Variable
    if ('tagname' not in req or
        (not isinstance(req['tagname'], str) and
        not isinstance(req['tagname'], list))
        ): return dict(error='key "tagname" missing')

    # Set Tagname
    tagname = req['tagname']

    # Set Default Value of Tag
    res = dict(name=None, value=None, status='Bad')

    # Try to Execute PyMes
    try: res = pypda.get(tagname)
    except: pass

    # Return Value
    return res

# Set Endnode Authentication
py_pda.user('client').password('sqw9eeq@2y2n985njwe34#')
    
#################################################################################################################################################

# PDA Check Status Endnode
@api.add('/api/isalive/')
def im_alive(req):
    return dict(alive=True)

#################################################################################################################################################

# start server
api.start()

# keep main thread alive
misc.keepalive()

#################################################################################################################################################
