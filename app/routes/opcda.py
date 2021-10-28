
#################################################################################################################################################

# Imports
import json
import flask
import py_misc
import OpenOPC

#################################################################################################################################################

Request = flask.request
Response = flask.Response

#################################################################################################################################################

# Create OPC Client
client = OpenOPC.client()
client.connect(opc_server='iba.ibaPdaOPC.1')

#################################################################################################################################################

# Load Routes
def __load__(app: py_misc.API):

    # Iba OPC-DA Read
    @app.route('/iba/opc/da/', methods=['POST'])
    def opcda(req: Request, res: Response):
        try: # Check Request Json
            if ('tags' not in req.json): raise Exception('key "tags" missing in request')
            if ('group' not in req.json): raise Exception('key "group" missing in request')
            if not isinstance(req.json['tags'], list): raise Exception('key "tags" not valid')
            if not isinstance(req.json['group'], str): raise Exception('key "group" not valid')
        except Exception as e:
            return res(
                json.dumps({ 'error': str(e) }),
                mimetype='application/json',
                status=200
            )
        # Set Variables
        tags = req.json['tags']
        group = req.json['group']
        # Read Tags from OPC Server
        read = client.read(tags=tags, group=group, update=1)
        # Return Value
        return res(
            json.dumps(read),
            mimetype='application/json',
            status=200
        )

    # Set Endnode Authentication
    opcda.user('iba.opc.client').password('sqw9eeq@2y2n985njwe34#')

#################################################################################################################################################
