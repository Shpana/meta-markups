from abc import abstractmethod
from typing import Iterable, NoReturn, Protocol, Type, TypeVar


TTarget = TypeVar("TTarget")
TMarkupOption = TypeVar("TMarkupOption")


class IMarkupContext(Protocol):

    @abstractmethod
    def add_option(self, 
            target: TTarget, option: TMarkupOption) -> NoReturn: 
        """ Добавляет опцию разметки """

    @abstractmethod
    def has_option(self, 
            target: TTarget, option_type: Type[TMarkupOption]) -> bool: 
        """ Проверяет имеет ли объект переданную опцию """

    @abstractmethod
    def select_all_options(self, target: TTarget) -> Iterable[TMarkupOption]:
        """ Возвращает все имеющиеся опции разметки """

    @abstractmethod
    def select_options(self, 
            target: TTarget, options_type: Type[TMarkupOption]) -> Iterable[TMarkupOption]: 
        """ Возвращает все опции, привязянные к объекту, с переданным типом """
