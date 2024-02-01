from typing import Type, TypeVar, Hashable

from .markup_context import IMarkupContext, TTarget, TMarkupAttribute


TRealTarget = TypeVar("TRealTarget", bound=TTarget.__bound__ | Hashable)


class RuntimeMarkupContext(IMarkupContext): 

    def __init__(self) -> None:
        self.__markup = dict()

    def attach_attribute(self, 
            target: TRealTarget, attr: TMarkupAttribute) -> None: 
        if not self.has_target(target):
            self.__markup[target] = list()
        self.__markup[target].append(attr)

    def has_target(self, target: TRealTarget) -> bool:
        return target in self.__markup

    def has_attribute_with_type(self, 
            target: TRealTarget, attr_type: Type[TMarkupAttribute]) -> bool:
        return (
            self.has_target(target)
            and
            any(map(lambda attr: type(attr) is attr_type, self.__markup[target])))

    def get_attributes(self, target: TRealTarget) -> tuple[TMarkupAttribute]:
        self.__guard_accessing(target)
        return (attr for attr in self.__markup[target])

    def get_attributes_with_type(self, 
            target: TRealTarget, attr_type: Type[TMarkupAttribute]) -> tuple[TMarkupAttribute]: 
        self.__guard_accessing(target)
        return tuple(filter(lambda attr: type(attr) is attr_type, self.__markup[target]))

    def __guard_accessing(self, target: TRealTarget) -> None: 
        if not self.has_target(target):
            raise ValueError(f"Target ({target}) not exists in current context. You cannot access its attributes.")
