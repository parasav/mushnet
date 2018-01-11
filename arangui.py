import eel
from arango import ArangoClient

eel.init('web')
@eel.expose
def arangoConnect(getIp, getPort, getUser, getPass, getNewdb):
	client = ArangoClient(
    	protocol='http',
    	host= getIp,
    	port=getPort,
    	username=getUser,
    	password=getPass,
   		enable_logging=True
	)
	print("connected?")
	try:
		client.create_database(getNewdb)
		print('Created new db, '+ getNewdb)
		return(client.databases())
	except:
		print('failed to create new DB, ' + getNewdb)

	print(client.databases())
	return(client.databases())


@eel.expose
def js_console(x):
	print(x)

eel.start('arangui.html', size=(400, 400))