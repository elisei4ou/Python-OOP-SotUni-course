from abc import ABC, abstractmethod


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class IContent(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def set_content(self):
        ...


class MyContent(IContent):

    def set_content(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class ISender(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def set_person(self):
        ...


class IMperson(ISender):

    def set_person(self):
        return ''.join(["I'm ", self.text])


class Email(IEmail):

    def __init__(self):
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: IMperson):
        self.__sender = sender.set_person()

    def set_receiver(self, receiver: IMperson):
        self.__receiver = receiver.set_person()

    def set_content(self, content: IContent):
        self.__content = content.set_content()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email()
sender = IMperson("Jamal")
receiver = IMperson("Ivan")

email.set_sender(sender)
email.set_receiver(receiver)

content = MyContent('Hello, there!')

email.set_content(content)

print(email)
