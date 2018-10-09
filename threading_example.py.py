import threading


class KevinsMessenger(threading.Thread):
    def run(self):
        for _ in range(100):
            print(threading.currentThread().getName())


obj1 = KevinsMessenger(name="Send out Messages")
obj2 = KevinsMessenger(name="Receive Messages")


obj1.start()
obj2.start()
