from multiprocessing import Value
from typing import Type, Dict
from abstracts.command import Command
from commands.say_hello_person import SayHelloPerson
from commands.say_hello_world import SayHelloWorld


class CommandFactory:
    @staticmethod
    def create_command(command_type: str, **kwargs) -> Command:

        command: Dict[str, Type[Command]] = {
            "say_hello_world": SayHelloWorld,
            "say_hello_person": SayHelloPerson,
        }

        command_class = command.get(command_type)
        if not command_class:
            raise ValueError(f"Unknown command type: {command_type}")

        return command_class(**kwargs)
