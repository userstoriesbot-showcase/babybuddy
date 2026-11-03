# Showcase fork only: development settings that sign every visitor in as the
# default "admin" user that the migrations create, so a demo run needs no login.
from .development import *  # noqa: F401,F403

MIDDLEWARE = MIDDLEWARE + ["babybuddy.showcase_autologin.AutoLogin"]  # noqa: F405
