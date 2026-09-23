#F1
class Notification:
    def send(self):
        return "notification"

#F2, F3
class EmailNotification(Notification):
    def send(self):
        return "Email notification"

class SMSNotification(Notification):
    def send(self):
        return "SMS notification"

#F4
print(Notification().send())
print(EmailNotification().send())
print(SMSNotification().send())

#F5
#They all use their own send method, if one of child classes lacked a send method it would have used the send method from the parent class
