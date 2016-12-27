import os
import sys
from lutris import settings


def get():
    """Return the path for the resources."""
    return '/app/share/lutris'


def get_banner_path(slug):
    return os.path.join(settings.BANNER_PATH, "%s.jpg" % slug)


def get_icon_path(slug):
    return os.path.join(settings.ICON_PATH, "lutris_%s.png" % slug)
