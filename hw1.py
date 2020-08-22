from abc import ABC


# A contact contains a name and telephone number
class Contact:
    name = ''
    tele = ''

    # constructor
    def __init__(self, n, telephone):
        self.name = n
        self.tele = telephone

    # string tells contact's name and number
    def tostring(self):
        print('Contact Info: %s, %s' % self.name % self.tele)

    # get name of contact
    def get_name(self): return self.name

    # get number of contact
    def get_number(self): return self.tele


# an event has a contact and a date and time
class Event(ABC):
    contact = ''
    date_time = ''

    # constructor
    def __init__(self, c, dt):
        self.contact = c
        self.date_time = dt

    # string show who's the event with and the date and time
    def tostring(self):
        print('Event with %s on %s' % (self.contact.name, self.date_time))


# An appointment has a type
class Appointment(Event):
    apt_type = ''

    # constructor uses attributes from Event class
    def __init__(self, apt_type, contact, date_time):
        Event.__init__(self, contact, date_time)
        self.apt_type = apt_type

    # string tell what type of appointment with who and the date and time
    def tostring(self):
        print('%s appointment for %s on %s' % (self.apt_type, self.contact.name, self.date_time))

    # getter method for appointment type
    def get_type(self): return self.apt_type


# A meeting contains a list of attendees
class Meeting(Event):
    attendees = []

    # constructor uses attributes from Event class
    def __init__(self, attendees, contact, date_time):
        Event.__init__(self, contact, date_time)
        self.attendees = attendees

    # String tell who the meeting is hosted by and the date and time
    def tostring(self):
        print('Meeting hosted by  %s at %s' % (self.contact.name, self.date_time))

    # adds attendee to the attendee lise
    def add_attendee(self, name):
        self.attendees.append(name)

    # gets attendees in a meeting
    def get_attendees(self):
        for i in range(0, len(self.attendees)):
            print(self.attendees[i])


# An appointment book has a list of events
class AppointmentBook:
    event_list = []

    # constructor
    def __init__(self, event_list):
        self.event_list = event_list

    # add event to the appointment book
    def add_event(self, event):
        for i in range(0, len(self.event_list)):
            if event.date_time == self.event_list[i].date_time:
                print('Event conflicted with another event')
                return

        self.event_list.append(event)
        print('Event added to appointment book.')

    # get events from appointment book with the same date
    def get_events_for_date(self, date_time):
        for i in range(0, len(self.event_list)):
            current_event = self.event_list[i].date_time
            if date_time == current_event[:current_event.index(' ')]:
                print(Event.tostring(self.event_list[i]))


# main method
def main():

    # making contacts, appointments, and meetings
    contact1 = Contact('Jane', '704-339-7649')
    contact2 = Contact('Sam', '919-393-8394')
    contact3 = Contact('Paul', '839-394-0495')
    contact4 = Contact('Thomas', '334-493-3404')
    contact5 = Contact('Amanda', '919-203-3049')
    contact6 = Contact('Tony', '335-394-2380')
    appt1 = Appointment('Doctor', contact1, '10/3/2025 at 10 a.m.')
    appt2 = Appointment('Doctor', contact2, '11/24/2020 at 12 p.m.')
    meeting1 = Meeting(['John', 'Kate', 'Mary'], contact3, '08/11/2021 at 3 p.m.')
    meeting2 = Meeting(['Bella', 'Emely', 'Sarah', 'Jake'], contact4, '01/03/2021 at 8 a.m.')
    addmeeting1 = Meeting(['Maggie', "Amelia"], contact5, '01/03/2021 at 8 a.m.')
    addmeeting2 = Meeting(['Joe'], contact6, "01/03/2021 at 9 a.m.")

    # add events to appointment book
    eventlist = [appt1, appt2, meeting1, meeting2]
    appt_book = AppointmentBook(eventlist)

    # Display appointment 1 and Meeting 1
    Appointment.tostring(eventlist[1])
    Meeting.tostring(eventlist[2])

    # test get_name method and get_number method for appointment
    print('Appointment 1 is for: %s, %s' % (appt1.contact.get_name(), appt1.contact.get_number()))

    # Add attendee and display attendees for meeting 2
    print('Attendees for Meeting 2: ')
    Meeting.add_attendee(eventlist[3], 'Seth')
    Meeting.get_attendees(eventlist[3])

    # test get_type method for appointment
    print('%s\'s appointment is a %s appointment' % (eventlist[0].contact.name, eventlist[0].get_type()))

    # adding events to appointment book, testing conflicting events
    AppointmentBook.add_event(appt_book, addmeeting1)
    AppointmentBook.add_event(appt_book, addmeeting2)

    # getting events on the same date
    AppointmentBook.get_events_for_date(appt_book, '01/03/2021')


# run main
if __name__ == "__main__":
    main()
