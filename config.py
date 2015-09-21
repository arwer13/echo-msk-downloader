#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime

from common import *


publishing_delay = datetime.timedelta(hours=8)
output_dir = "Audiobooks"


programmes = [
    {
        "code": "code",
        "name": "Код доступа",
        "time": datetime.time(19, 7),
        "dow": Dow.Saturday
    },
    {
        "code": "sut",
        "name": "Суть событий",
        "time": datetime.time(21, 7),
        "dow": Dow.Friday
    }
]
