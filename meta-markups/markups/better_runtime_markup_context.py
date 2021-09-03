from typing import NoReturn, Iterable, Type

from .markup_context import IMarkupContext, TTarget, TMarkupOption


class BetterRuntimeMarkupContext(IMarkupContext):
    
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
            any(map(lambda option: type(option) is option_type, self.__meta_markups[target])))

    def select_all_options(self, target: TTarget) -> Iterable[TMarkupOption]:
        result_markups = []
        if self.__target_exists(target):
            result_markups = self.__meta_markups[target]

        return (option for option in result_markups)

    def select_options(self, 
            target: TTarget, options_type: Type[TMarkupOption]) -> Iterable[TMarkupOption]: 
        result_markups = []
        if self.__target_exists(target):
            result_markups = self.__meta_markups[target]

        return filter(lambda option: type(option) is options_type, result_markups)

    def __target_exists(self, target: TTarget) -> bool:
        return target in self.__meta_markups
