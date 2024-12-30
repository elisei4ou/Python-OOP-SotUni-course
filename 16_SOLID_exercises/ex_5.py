from abc import ABC, abstractmethod


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class IContent(ABC):

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail, IContent):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == "IM":
            self.__sender = f"I am {sender}"
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == "IM":
            self.__receiver = f"I am {receiver}"
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content.set_content(content)

    def __repr__(self):
        return f"Sender: {self.__sender}\n" \
               f"Receiver: {self.__receiver}\n" \
               f"Content:\n" \
               f"{self.__content}"


class MyContent(IContent):
    def __init__(self, content):
        self.content = content

    def set_content(self, content):
        return f"<MyML>{self.content}</MyML>"


email = Email("IM")
email.set_sender("qmal")
email.set_receiver("james")
content = MyContent("Hello, there!")
email.set_content(content)
print(email)
