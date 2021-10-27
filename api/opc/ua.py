
#################################################################################################################################################

# Imports
import json
import flask
import py_misc

#################################################################################################################################################

Request = flask.request
Response = flask.Response

#################################################################################################################################################

# Create OPC Client
opcget = (lambda tags, group: { 'nothing': None })

#################################################################################################################################################

# Load Routes
def __load__(api: py_misc.API):

    # Iba OPC-DA Read
    @api.route('/iba/opc/ua/', methods=['POST'])
    def opcua(req: Request, res: Response):
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
        read = opcget(tags=tags, group=group)
        # Return Value
        return res(
            json.dumps(read),
            mimetype='application/json',
            status=200
        )

    # Set Endnode Authentication
    opcua.user('iba.opc.client').password('sqw9eeq@2y2n985njwe34#')

#################################################################################################################################################
