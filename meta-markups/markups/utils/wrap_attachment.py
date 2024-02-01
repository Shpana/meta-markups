from ..markup_context import IMarkupContext, TMarkupAttribute, TTarget


def wrap_attachment(
        context: IMarkupContext, 
        target: TTarget, attr: TMarkupAttribute) -> TTarget:
    context.attach_attribute(target, attr)
    return target
