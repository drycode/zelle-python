
import json as json

class ConferenceManager:
    def __init__(self):
        self.attendees = []
        filename = open('conferenceAttendees.json', 'r')
        json_string = filename.read()        
        self.json_object = json.loads(json_string)
        for k in self.json_object.keys():
            a = Attendee(self.json_object[k]["name"], self.json_object[k]["company"], self.json_object[k]["state"], k)
            self.attendees.append(a)
        filename.close()
        
    def getJSON(self):
        return self.json_object
    
    def getAttendee(self, name):
        for attendee in self.attendees:
            if attendee.getName() == name:
                return attendee

    def findByState(self, state):
        results = []
        for attendee in self.attendees:
            if attendee.getState() == state:   
                results.append(attendee)
        return results
        
    def makeAttendee(self, name, company, state, email):
        attendee = Attendee(name, company, state, email)
        self.attendees.append(attendee)
    
    def delAttendee(self, name):
        for attendee in self.attendees:
            if attendee.getName():
                attendee.pop(attendee)

    def updateConference(self):
        data = []
        for attendee in self.attendees:
                data.append(vars(attendee))
        with open('conferencedAttendees1.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
        

class Attendee:
    def __init__(self, name, company, state, email):
        self.name = name
        self.company = company
        self.state = state
        self.email = email
        self.attendee = [self.name, self.company, self.state, self.email]

    def getName(self):
        return self.name

    def getCompany(self):
        return self.company

    def getState(self):
        return self.state
    
    def getEmail(self):
        return self.email

    def displayInfo(self):
        print("{0}  {1} {2} {3}".format(self.name, self.company, self.state, self.email))

def main():
    conference = ConferenceManager()
    conference.makeAttendee("Carson", "Philadelphia Eagles", "PA, USA", "wentz@philaeagles.com")
    sean = conference.getAttendee("Carson")
    list = conference.findByState("PA, USA")
    print(sean.getCompany())
    print(sean.getName())
    print(sean.getState())
    print(sean.getEmail())
    sean.displayInfo()
    conference.updateConference()
    for per in list:
        print(per.getName())

main()