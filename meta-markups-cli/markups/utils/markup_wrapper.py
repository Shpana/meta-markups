from ..markup_context import IMarkupContext, TMarkupOption, TTarget


def markup_wrapper(
        context: IMarkupContext, target: TTarget, option: TMarkupOption) -> TTarget:
    context.add_option(target, option)
    return target
