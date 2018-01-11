import eel
from arango import ArangoClient

eel.init('web')
@eel.expose
def arangoConnect(getIp, getPort, getUser, getPass):
	client = ArangoClient(
    	protocol='http',
    	host= getIp,
    	port=getPort,
    	username=getUser,
    	password=getPass,
   		enable_logging=True
	)
	print("connected?")
	print(client.databases())

eel.start('arangui.html', size=(400, 200))