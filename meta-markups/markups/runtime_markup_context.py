from typing import NoReturn, Iterable, Type

from .markup_context import IMarkupContext, TTarget, TMarkupOption


class RuntimeMarkupContext(IMarkupContext): 

    def __init__(self) -> NoReturn:
        self.__meta_markups = dict()

    def add_option(self, 
            target: TTarget, option: TMarkupOption) -> NoReturn: 
        if not self.__target_exists(target):
            self.__meta_markups[target] = list()

        self.__meta_markups[target].append(option)

    def has_option(self, 
            target: TTarget, option_type: Type[TMarkupOption]) -> bool:
        return (
            self.__target_exists(target) 
            and
            any(map(lambda option: type(option) is option_type), self.__meta_markups[target]))

    def select_all_options(self, target: TTarget) -> Iterable[TMarkupOption]:
        self.__guard_selection(target)

        return (option for option in self.__meta_markups[target])

    def select_options(self, 
            target: TTarget, options_type: Type[TMarkupOption]) -> Iterable[TMarkupOption]: 
        self.__guard_selection(target)

        return filter(lambda option: type(option) is options_type, self.__meta_markups[target])

    def __target_exists(self, target: TTarget) -> bool:
        return target in self.__meta_markups

    def __guard_selection(self, target: TTarget) -> NoReturn: 
        if not self.__target_exists(target):
            raise ValueError(f"Target {target} not exists. You cannot select options from it.")
