import eel

eel.init('web')

@eel.expose
def get_output(input):
	print('Got ' + input + ".")
	return input + input

eel.start('eelgui.html', size=(320, 120))