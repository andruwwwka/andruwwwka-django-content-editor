from django import template

register = template.Library()


@register.simple_tag(takes_context=False)
def editable_text(model, property, permission=True):
    if not permission:
        return model.__getattribute__(property)

    text = model.__getattribute__(property)

    model_name = model.__class__.__name__
    package = model.__class__.__module__
    if package is not None:
        model_name = package + '.' + model_name
    row = str(model.pk)

    info = model_name + '+' + property + '+' + row
    return '<div class="editable-text-wrap"><button type="button" class="edit-text" data-info="%s"></button>' \
           '<div class="editable-text" contenteditable="true">%s</div>' \
           '<div class="not-editable-text">%s</div></div>' % (info, text, text)
