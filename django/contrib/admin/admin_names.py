# coding: utf-8

from django.conf import settings
from django.utils.translation import ugettext as _


def extended_verbose_name(request, opts, action=None):
    language = getattr(request, 'LANGUAGE_CODE', None)
    verbose_name_extended = getattr(opts, 'verbose_name_extended', {})
    options = verbose_name_extended.get(language)

    if options:
        return options.get(action, opts.verbose_name)
    else:
        return _(opts.verbose_name)


def change_label(label):
    app_labels = getattr(settings, 'APP_LABELS', {})
    app_name = app_labels.get(label.lower(), label)

    return _(app_name)
