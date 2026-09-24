#A1, A2
class EmailNotification:
    def send(self):
        return "Email"

class SMSNotification:
    def send(self):
        return "SMS"

class PushNotification:
    def send(self):
        return "Push"

#A3
notification_list = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

#A4
for notification in notification_list:
    print(notification.send())

#A5
#As long as each object has a send() method, it will be called #polymorphism
