from abc import ABC, abstractmethod

class IChannel(ABC):
    @abstractmethod
    def subscriber(self, subscriber):
        pass

    @abstractmethod
    def unsubsciber(self, subscriber):
        pass

    @abstractmethod
    def notify_subscriber(self):
        pass


class ISubscriber(ABC):
    @abstractmethod
    def update(self):
        pass


class Channel(IChannel):
    def __init__(self, name):
        self.subscribers = [] 
        self.name = name
        self.latest_video = None

    def subscriber(self, subscriber): 
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def unsubsciber(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify_subscriber(self):
        for subscriber in self.subscribers:
            subscriber.update(self.name, self.latest_video)  

    def upload_video(self, title):
        self.latest_video = title
        print(f"Uploading video '{title}' to channel '{self.name}'")
        self.notify_subscriber()

class Subscriber(ISubscriber):
    def __init__(self, name):
        self.name = name

    def update(self, channel_name, video_title):
        print(f"{self.name} got notified! New video '{video_title}' uploaded on channel '{channel_name}'.")

if __name__ == "__main__":

    channel = Channel("My Channel")

 
    subscriber = Subscriber('User 1')

    channel.subscriber(subscriber)

    title = input('Write the title of the video: ')
    channel.upload_video(title)
