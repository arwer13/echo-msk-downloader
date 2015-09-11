#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError
import datetime
import os

import config

g_base_url = "http://cdn.echo.msk.ru/snd"


def get_last_program_time(pr):
    threshold = datetime.datetime.now() - config.publishing_delay
    the_time = datetime.datetime(threshold.year, threshold.month, threshold.day, pr["time"].hour, pr["time"].minute)
    while the_time >= threshold or the_time.weekday() != pr["dow"].value:
        the_time -= datetime.timedelta(days=1)
    return the_time


def get_episode_path(pr, dt):
    return os.path.join(make_programme_folder(pr), episode_file_name(pr, dt))


def was_downloaded(pr, dt):
    return os.path.exists(get_episode_path(pr, dt))


def make_programme_folder(pr):
    folder_path = os.path.join(config.output_dir, pr["name"])
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def episode_file_name(pr, dt):
    return "{}-{}-{}.mp3".format(dt.strftime("%Y-%m-%d"), pr["code"], pr["time"].strftime("%H%M"))


def make_url(pr, dt):
    return "{}/{}".format(g_base_url, episode_file_name(pr, dt))


def download(pr, dt):
    ep_path = get_episode_path(pr, dt)
    url = make_url(pr, dt)
    episode_name = episode_file_name(pr, dt)
    try:
        with urlopen(url) as rr, open(ep_path, "wb") as ff:
            ff.write(rr.read())
            print("Episode {} downloaded.".format(episode_name))
    except HTTPError:
        print("Can't download {}. Maybe it's not published yet?".format(episode_file_name(pr, dt)))


if __name__ == '__main__':
    for p in config.programmes:
        last_program_time = get_last_program_time(p)
        if not was_downloaded(p, last_program_time):
            download(p, last_program_time)
        else:
            print("Episode {} was ALREADY downloaded.".format(episode_file_name(p, last_program_time)))
