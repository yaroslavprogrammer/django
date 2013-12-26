from django import template
from django.contrib.admin.admin_names import \
    extended_verbose_name, change_label

register = template.Library()


@register.simple_tag(takes_context=True)
def admin_verbose_name(context, opts, action=None):
    return extended_verbose_name(context['request'], opts, action)


@register.filter
def admin_change_label(label):
    return change_label(label)
