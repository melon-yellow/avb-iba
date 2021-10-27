
#################################################################################################################################################

# Imports
import py_misc

# Modules
from . import routes

#################################################################################################################################################

# Declare HTTP API
api = py_misc.API().host('0.0.0.0').port(3000)

#################################################################################################################################################

# Load Routes
routes.__load__(api)

#################################################################################################################################################

# start server
api.start()

# keep main thread alive
py_misc.keepalive()

#################################################################################################################################################