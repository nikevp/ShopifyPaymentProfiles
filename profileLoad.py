import tkinter
import requests
import json
from functools import partial


buttonStore = []
lastLocation = 0



def saveProfile(): #NOTE Saves Payment Profile.
	global lastLocation
	ValidationCheck = False

	profile = {'email': emailEntry.get(), 'firstName': firstNameEntry.get(), 'lastName': lastNameEntry.get(), 'address1': addressEntry.get(), 'city': cityEntry.get(), 'address2': address2Entry.get(), 'stateFull': stateFullEntry.get(),
	 'zipcode': zipEntry.get(), 'phone': phoneEntry.get(), 'creditCard': creditCardEntry.get(), 'creditMonth': creditMonthEntry.get(), 'creditYear': creditYearEntry.get(), 'creditCvv': creditCvvEntry.get(), 'proxy': proxyEntry.get()}
	
	for x in buttonStore:
		if x['email'] == profile['email']:
			x['button'].updateButton(profile)
			x['button'].placeButton()
			ValidationCheck = True
			break
	if ValidationCheck == True:
		print('updated exisiting profile')
		writeFile()
	else:
		button = createButton(lastLocation, profile)
		button.placeButton()
		buttonDict = {'email': profile['email'], 'button': button}
		buttonStore.append(buttonDict)
		lastLocation += 25
		writeFile()


def writeFile():
	tempSaveList = []
	for x in buttonStore:
		tempSaveList.append(x['button'].profile)
	savefile = open("profiles.json", "w")
	savefile.write(json.dumps(tempSaveList))

def loadFile():
	try:
		savefile = open("profiles.json")
		profileList = json.loads(savefile.read())
	except:
		profileList = []
	return profileList

def loadIT(profile):
	print('Loading')
	firstNameVar.set(profile['firstName'])
	lastNameVar.set(profile['lastName'])
	emailVar.set(profile['email'])
	addressVar.set(profile['address1'])
	cityVar.set(profile['city'])
	address2Var.set(profile['address2'])
	stateFullVar.set(profile['stateFull'])
	zipVar.set(profile['zipcode'])
	phoneVar.set(profile['phone'])
	creditCardVar.set(profile['creditCard'])
	creditMonthVar.set(profile['creditMonth'])
	creditYearVar.set(profile['creditYear'])
	creditCvvVar.set(profile['creditCvv'])
	proxyVar.set(profile['proxy'])

def displayProfiles(): #NOTE issue with previous method: old buttons aren't removed. Solution use classes to edit/update existing or add new
	global lastLocation
	initialSpot = 100
	for x in profileList:
		button = createButton(initialSpot, x)
		button.placeButton()
		buttonDict = {'email': x['email'], 'button': button}
		buttonStore.append(buttonDict)
		initialSpot += 25
		print(button.profile)
	lastLocation = initialSpot

class createButton(object):
	def __init__(self, vertLocation, profile):
		self.profile = profile
		self.vertLocation = vertLocation

	def updateButton(self, newProfile):
		self.profile = newProfile

	def placeButton(self):
		action_with_arg = partial(loadIT, self.profile)
		runButton = tkinter.Button(root, text =str(self.profile['email']), command = action_with_arg)
		runButton.pack(side="top")
		runButton.place(x = 500,y = self.vertLocation)






'''
GUI Code Below this point
'''
profileList = loadFile()
root = tkinter.Tk()

root.title("Manage Checkout Slots")

my_canvas = tkinter.Canvas(root, width=1000, height=500)
my_canvas.pack()

var = tkinter.StringVar()
label = tkinter.Label(root, textvariable=var, relief="flat", font=("Futura", 40), fg="black")
var.set("Manage Shopify Profiles")
label.pack(fill='both', expand='yes')
label.place(x = 50,y = 0)

result = tkinter.StringVar()
resultLabel = tkinter.Label(root, textvariable=result, relief="flat", font=("Futura", 20), fg="black")
result.set("Waiting...")
resultLabel.pack(fill='both', expand='yes')
resultLabel.place(x = 350,y = 300)

#First Name Entry
firstNameLabel = tkinter.Label(root, text="First Name", relief="flat", font=("Futura", 16), fg="black")
firstNameLabel.pack(fill='both', expand='yes')
firstNameLabel.place(x = 50,y = 75)
firstNameVar = tkinter.StringVar()
firstNameEntry = tkinter.Entry(root, textvariable=firstNameVar, relief='ridge')
firstNameEntry.pack(side='top')
firstNameEntry.place(x = 50,y = 100)

#Last Name Entry
lastNameLabel = tkinter.Label(root, text="Last Name", relief="flat", font=("Futura", 16), fg="black")
lastNameLabel.pack(fill='both', expand='yes')
lastNameLabel.place(x = 50,y = 125)
lastNameVar = tkinter.StringVar()
lastNameEntry = tkinter.Entry(root, textvariable=lastNameVar, relief='ridge')
lastNameEntry.pack(side='top')
lastNameEntry.place(x = 50,y = 150)

#Address Entry
addressLabel = tkinter.Label(root, text="Address", relief="flat", font=("Futura", 16), fg="black")
addressLabel.pack(fill='both', expand='yes')
addressLabel.place(x = 50,y = 175)
addressVar = tkinter.StringVar()
addressEntry = tkinter.Entry(root, textvariable=addressVar, relief='ridge')
addressEntry.pack(side='top')
addressEntry.place(x = 50,y = 200)

#StateAbrev Entry stateAbrev
address2Label = tkinter.Label(root, text="Address2", relief="flat", font=("Futura", 16), fg="black")
address2Label.pack(fill='both', expand='yes')
address2Label.place(x = 50,y = 225)
address2Var = tkinter.StringVar()
address2Entry = tkinter.Entry(root, textvariable=address2Var, relief='ridge')
address2Entry.pack(side='top')
address2Entry.place(x = 50,y = 250)

#City Entry
cityLabel = tkinter.Label(root, text="City", relief="flat", font=("Futura", 16), fg="black")
cityLabel.pack(fill='both', expand='yes')
cityLabel.place(x = 50,y = 275)
cityVar = tkinter.StringVar()
cityEntry = tkinter.Entry(root, textvariable=cityVar, relief='ridge')
cityEntry.pack(side='top')
cityEntry.place(x = 50,y = 300)

#stateFull
stateFullLabel = tkinter.Label(root, text="State (Full)", relief="flat", font=("Futura", 16), fg="black")
stateFullLabel.pack(fill='both', expand='yes')
stateFullLabel.place(x = 50,y = 325)
stateFullVar = tkinter.StringVar()
stateFullEntry = tkinter.Entry(root, textvariable=stateFullVar, relief='ridge')
stateFullEntry.pack(side='top')
stateFullEntry.place(x = 50,y = 350)

#Zip Entry
zipLabel = tkinter.Label(root, text="Zip", relief="flat", font=("Futura", 16), fg="black")
zipLabel.pack(fill='both', expand='yes')
zipLabel.place(x = 50,y = 375)
zipVar = tkinter.StringVar()
zipEntry = tkinter.Entry(root, textvariable=zipVar, relief='ridge')
zipEntry.pack(side='top')
zipEntry.place(x = 50,y = 400)

#creditCard Entry
creditCardLabel = tkinter.Label(root, text="Credit Card Number", relief="flat", font=("Futura", 16), fg="black")
creditCardLabel.pack(fill='both', expand='yes')
creditCardLabel.place(x = 250,y = 75)
creditCardVar = tkinter.StringVar()
creditCardEntry = tkinter.Entry(root, textvariable=creditCardVar, relief='ridge')
creditCardEntry.pack(side='top')
creditCardEntry.place(x = 250,y = 100)

#creditMonth Entry
creditMonthLabel = tkinter.Label(root, text="Credit Card Month (XX)", relief="flat", font=("Futura", 16), fg="black")
creditMonthLabel.pack(fill='both', expand='yes')
creditMonthLabel.place(x = 250,y = 125)
creditMonthVar = tkinter.StringVar()
creditMonthEntry = tkinter.Entry(root, textvariable=creditMonthVar, relief='ridge')
creditMonthEntry.pack(side='top')
creditMonthEntry.place(x = 250,y = 150)

#creditYear Entry
creditYearLabel = tkinter.Label(root, text="Credit Card Year (XXXX)", relief="flat", font=("Futura", 16), fg="black")
creditYearLabel.pack(fill='both', expand='yes')
creditYearLabel.place(x = 250,y = 175)
creditYearVar = tkinter.StringVar()
creditYearEntry = tkinter.Entry(root, textvariable=creditYearVar, relief='ridge')
creditYearEntry.pack(side='top')
creditYearEntry.place(x = 250,y = 200)

#creditCvv Entry
creditCvvLabel = tkinter.Label(root, text="Credit Card CVV", relief="flat", font=("Futura", 16), fg="black")
creditCvvLabel.pack(fill='both', expand='yes')
creditCvvLabel.place(x = 250,y = 225)
creditCvvVar = tkinter.StringVar()
creditCvvEntry = tkinter.Entry(root, textvariable=creditCvvVar, relief='ridge')
creditCvvEntry.pack(side='top')
creditCvvEntry.place(x = 250,y = 250)

#Phone Entry
phoneLabel = tkinter.Label(root, text="Mobile Phone", relief="flat", font=("Futura", 16), fg="black")
phoneLabel.pack(fill='both', expand='yes')
phoneLabel.place(x = 250,y = 275)
phoneVar = tkinter.StringVar()
phoneEntry = tkinter.Entry(root, textvariable=phoneVar, relief='ridge')
phoneEntry.pack(side='top')
phoneEntry.place(x = 250,y = 300)

#email Entry
emailLabel = tkinter.Label(root, text="Email Address", relief="flat", font=("Futura", 16), fg="black")
emailLabel.pack(fill='both', expand='yes')
emailLabel.place(x = 250,y = 325)
emailVar = tkinter.StringVar()
emailEntry = tkinter.Entry(root, textvariable=emailVar, relief='ridge')
emailEntry.pack(side='top')
emailEntry.place(x = 250,y = 350)

#proxy Entry
proxyLabel = tkinter.Label(root, text="Proxy (127.0.0.0:8080) or None", relief="flat", font=("Futura", 16), fg="black")
proxyLabel.pack(fill='both', expand='yes')
proxyLabel.place(x = 250,y = 375)
proxyVar = tkinter.StringVar()
proxyEntry = tkinter.Entry(root, textvariable=proxyVar, relief='ridge')
proxyEntry.pack(side='top')
proxyEntry.place(x = 250,y = 400)

proxyLabel = tkinter.Label(root, text="Proxy (127.0.0.0:8080) or None", relief="flat", font=("Futura", 16), fg="black")
proxyLabel.pack(fill='both', expand='yes')
proxyLabel.place(x = 250,y = 375)
proxyVar = tkinter.StringVar()
proxyEntry = tkinter.Entry(root, textvariable=proxyVar, relief='ridge')
proxyEntry.pack(side='top')
proxyEntry.place(x = 250,y = 400)

profilesLabel = tkinter.Label(root, text="Currently Saved Profiles", relief="flat", font=("Futura", 16), fg="black")
profilesLabel.pack(fill='both', expand='yes')
profilesLabel.place(x = 500,y = 75)


displayProfiles()

runButton = tkinter.Button(root, text ="Save Profile", command = saveProfile)
runButton.pack(side="top")
runButton.place(x = 200,y = 450)

tkinter.mainloop()
