class EventSystem:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event, callback):
        self.listeners.setdefault(event, []).append(callback)

    def emit(self, event, data):
        for callback in self.listeners.get(event, []):
            callback(data)

def email_notification(data):
    print("📧 Email sent:", data)

def sms_notification(data):
    print("📱 SMS sent:", data)

es = EventSystem()
es.subscribe("order_placed", email_notification)
es.subscribe("order_placed", sms_notification)

es.emit("order_placed", "Order #123 confirmed")
