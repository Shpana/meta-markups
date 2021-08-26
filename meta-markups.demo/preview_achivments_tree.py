from pprint import pprint
from typing import Callable, NoReturn, Type
from dataclasses import dataclass
from abc import abstractmethod, abstractproperty

from markups import apply_option, load_options


class Achievement: 

    @abstractproperty
    def points(self) -> int: ...

    @abstractproperty
    def description(self) -> str: ...

    @abstractmethod
    def can_achieve_expression(self) -> bool: ...


@dataclass
class RequireAchievementMarkupOption: 
    achievement_type: Type[Achievement]


def require(achievement_type: Type[Achievement]) -> Callable:
    return lambda target: apply_option(
        target, 
        RequireAchievementMarkupOption(achievement_type)
    )


class GoodJob(Achievement):

    @property
    def points(self) -> int: ...

    @property
    def description(self) -> str: ...

    def can_achieve_expression(self) -> bool: ...


@require(GoodJob)
class ExcelentJob(Achievement):

    @property
    def points(self) -> int: ...

    @property
    def description(self) -> str: ...

    def can_achieve_expression(self) -> bool: ...



class AchievementTree:

    def __init__(self, achievements: list[Achievement]) -> NoReturn:
        self.__tree = self.__parse_dependency_graph(achievements)

    def preview(self) -> NoReturn:
        pprint(self.__tree)
    
    Graph = dict[str, list[Type[Achievement]]]

    def __parse_dependency_graph(self, achievements: list[Achievement]) -> Graph:
        graph = dict()
        
        # TODO: Обработка циклов - их не должно быть.
        for achievement in achievements:
            graph[achievement] = list(load_options(type(achievement), RequireAchievementMarkupOption))
        else:
            return graph


if __name__ == "__main__":
    tree = AchievementTree([
        GoodJob(),
        ExcelentJob(),
    ])

    tree.preview()
