from dataclasses import dataclass
from abc import abstractmethod
from typing import Callable, Iterable, NoReturn, Protocol, Type, TypeVar


TTarget = TypeVar("TTarget")
TMarkupOption = TypeVar("TMarkupOption")


@dataclass
class OptionLink:

    # TODO: Ссылать на объект по-другому (возможно 
    # по его имени), хотя в рамках одного процесса это не важно

    target: TTarget
    option: TMarkupOption


class IMarkupContext(Protocol):

    @abstractmethod
    def add_link(self, target: TTarget, option: TMarkupOption) -> NoReturn: ...

    @abstractmethod
    def select_links(self, 
        target: TTarget, option_type: Type[TMarkupOption]) -> Iterable[TMarkupOption]: ...


class RuntimeMarkupContext(IMarkupContext):
    
    def __init__(self) -> NoReturn:
        self.__links = list()

    def add_link(self, target: TTarget, option: TMarkupOption) -> NoReturn:
        self.__links.append(OptionLink(target, option))

    def select_links(self, 
            target: TTarget, 
            option_type: Type[TMarkupOption]) -> Iterable[TMarkupOption]:
        
        return filter(
            lambda link: link.target is target and type(link.option) is option_type, self.__links
        )


class MarkupContextFactory:

    # TODO: Загрузка информации о контексте разметки
    
    def generate_context(self) -> IMarkupContext:
        return RuntimeMarkupContext()


context = MarkupContextFactory().generate_context()


def apply_option(target: TTarget, option: TMarkupOption) -> Callable:
    context.add_link(target, option)
    return target


def load_options(target: TTarget, option_type: Type[TMarkupOption]) -> tuple[TMarkupOption]:
    return tuple(
        map(lambda link: link.option, context.select_links(target, option_type))
    )
