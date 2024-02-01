from abc import abstractmethod
from typing import Type, TypeVar


TTarget = TypeVar("TTarget")
TMarkupAttribute = TypeVar("TMarkupAttribute")


class IMarkupContext:

    @abstractmethod
    def attach_attribute(self, 
            target: TTarget, attr: TMarkupAttribute) -> None: ...

    @abstractmethod
    def has_target(self, target: TTarget) -> bool: ...

    @abstractmethod
    def has_attribute_with_type(self, 
            target: TTarget, attr_type: Type[TMarkupAttribute]) -> bool: ...

    @abstractmethod
    def get_attributes(self, target: TTarget) -> tuple[TMarkupAttribute]: ...

    @abstractmethod
    def get_attributes_with_type(self,
            target: TTarget, attr_type: Type[TMarkupAttribute]) -> tuple[TMarkupAttribute]: ...

    def try_get_attributes(self, target: TTarget) -> tuple[TMarkupAttribute]:
        if not self.has_target(target):
            return tuple()
        else:
            return self.get_attributes(target)
    
    def try_get_attributes_with_type(self, 
            target: TTarget, attr_type: Type[TMarkupAttribute]) -> tuple[TMarkupAttribute]:
        if not self.has_target(target):
            return tuple()
        else:
            return self.get_attributes_with_type(target, attr_type)
