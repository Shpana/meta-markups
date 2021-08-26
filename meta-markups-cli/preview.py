from argparse import ArgumentParser
from typing import NoReturn, TypeVar

from options import \
    alias, select_aliases, title, select_title

from options import with_attribute, select_attributes


@title("hello")
@alias("hi")
def hello_command(_) -> NoReturn: 
    print("hello world")


@title("print")
@with_attribute("message", type=str)
def print_command(args) -> NoReturn:
    print(args.message)


TCommand = TypeVar("TCommand")

class App:

    def __init__(self) -> NoReturn:
        self.__parser = ArgumentParser()
        self.__subparser = self.__parser.add_subparsers()

    def run(self) -> NoReturn:
        args = self.__parser.parse_args()
        args.func(args)

    def with_command(self, command: TCommand) -> NoReturn:
        subparser = self.__subparser.add_parser(
            select_title(command).value, 
            aliases=[alias.value for alias in select_aliases(command)])
        
        subparser.set_defaults(func=command)

        for attribute in select_attributes(command):
            subparser.add_argument(attribute.name, type=attribute.type)


if __name__ == "__main__":
    app = App()
    app.with_command(hello_command)
    app.with_command(print_command)
    app.run()
