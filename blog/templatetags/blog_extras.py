from django import template

register = template.Library()

@register.filter
def add_class(field, class_names):
    # Get any current classes set on the field
    field_classes = field.field.widget.attrs.get('class', '')
    # Append passed in classes
    field_classes += class_names
    # Set the new array to the field and return
    field.field.widget.attrs['class'] = field_classes
    return field
