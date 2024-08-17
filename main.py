import argparse
from multiprocessing import Value
from typing import Dict, Type, Union
from abstracts import command
from abstracts.command import Command
from commandFactory import CommandFactory
from commands.say_hello_world import SayHelloWorld


arguments_contract = {
    "say_hello_world": [],
    "say_hello_person": [
        {"name": "--name", "help": "Name to greet", "type": str, "required": True},
    ],
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="The command to execute", type=str)

    args = parser.parse_known_args()[0]

    if args.command in arguments_contract:
        for arg in arguments_contract[args.command]:
            parser.add_argument(
                arg.get("name"),
                help=arg.get("help"),
                type=arg.get("type"),
                required=arg.get("required"),
            )

    args = parser.parse_args()

    command_args = vars(args).copy()
    command_type = command_args.pop("command")

    try:
        command = CommandFactory.create_command(
            command_type=command_type, **command_args
        )
        command.run()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
