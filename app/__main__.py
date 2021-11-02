
#################################################################################################################################################

# Imports
import os
import py_misc

# Modules
from . import routes

#################################################################################################################################################

# Declare HTTP API
app = py_misc.API().host('0.0.0.0')
app.port(os.getenv('AVB_IBA_PORT'))

#################################################################################################################################################

# Load Routes
routes.__load__(app)

#################################################################################################################################################

# start server
app.start()

# keep main thread alive
py_misc.keepalive()

#################################################################################################################################################
