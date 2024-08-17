from abstracts.command import Command


class SayHelloWorld(Command):
    def run(self) -> None:
        print("Hello World")
