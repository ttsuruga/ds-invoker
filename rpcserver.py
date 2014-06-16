from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ()

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler,
			    allow_none=True)
server.register_introspection_functions()

def browser_function(url):
    browsercmd="iexplore.exe -k "+url
    #browsercmd="firefox "+url
    os.system(browsercmd)
server.register_function(browser_function, 'browse')

# Run the server's main loop
server.serve_forever()
