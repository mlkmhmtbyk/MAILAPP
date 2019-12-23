def CreateEvent (event):
    f = open("events.txt", "a+")
    f.write("\n"+ event)
    f.close()

def ReadEvents():
    f = open("events.txt", "r")
    contents =f.read()
    print(contents)
    f.close()

def SearchEvent(eventName):
    f = open("events.txt", "r")
    f1 = f.readlines()
    for i in f1:
        if (i.__contains__(eventName)):
            print(i)   	

def DeleteEvent(eventName):
	f = open("events.txt", "r+")
	f1 = f.readlines()
	for i in f1:
		if (i.__contains__(eventName)):
			f.truncate(i)  
	f.close()


DeleteEvent("Kahvaltı")

input('Press ENTER to exit')
