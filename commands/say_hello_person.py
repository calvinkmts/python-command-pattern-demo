from abstracts.command import Command


class SayHelloPerson(Command):
    def __init__(self, name: str):
        self.name = name

    def run(self):
        print(f"Hello {self.name}")
