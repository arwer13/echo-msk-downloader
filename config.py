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
    },
    {
        "code": "Diletanti",
        "name": "Дилетанты",
        "time": datetime.time(21, 7),
        "dow": Dow.Thursday
    },
    {
        "code": "netak",
        "name": "Не так",
        "time": datetime.time(12, 8),
        "dow": Dow.Sunday
    },
    #{
        #"code": "tabel",
        #"name": "Табель о рангах",
        #"time": datetime.time(12, 8),
        #"dow": Dow.Sunday
    #},
    {
        "code": "48minut",
        "name": "48 минут",
        "time": datetime.time(22, 7),
        "dow": Dow.Wednesday
    },
    {
        "code": "49minut",
        "name": "49 минут",
        "time": datetime.time(22, 7),
        "dow": Dow.Wednesday
    }
]
