from typing import Type

from .markup_context import IMarkupContext, TTarget, TMarkupAttribute


class RuntimeMarkupContext(IMarkupContext): 

    def __init__(self) -> None:
        self.__markup = dict()

    def attach_attribute(self, 
            target: TTarget, attr: TMarkupAttribute) -> None: 
        if not self.has_target(target):
            self.__markup[target] = list()
        self.__markup[target].append(attr)

    def has_target(self, target: TTarget) -> bool:
        return target in self.__markup

    def has_attribute_with_type(self, 
            target: TTarget, attr_type: Type[TMarkupAttribute]) -> bool:
        return (
            self.has_target(target)
            and
            any(map(lambda attr: type(attr) is attr_type, self.__markup[target])))

    def get_attributes(self, target: TTarget) -> tuple[TMarkupAttribute]:
        self.__guard_accessing(target)
        return (attr for attr in self.__markup[target])

    def get_attributes_with_type(self, 
            target: TTarget, attr_type: Type[TMarkupAttribute]) -> tuple[TMarkupAttribute]: 
        self.__guard_accessing(target)
        return filter(lambda attr: type(attr) is attr_type, self.__markup[target])

    def __guard_accessing(self, target: TTarget) -> None: 
        if not self.has_target(target):
            raise ValueError(f"Target ({target}) not exists in current context. You cannot access its attributes.")
