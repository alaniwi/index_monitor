# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from django.contrib import admin
import index_monitor_app.models as models

for name in dir(models):
    if re.match("^[A-Z]", name):
        admin.site.register(getattr(models, name))

