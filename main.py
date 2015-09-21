#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError
import datetime
import os

import config

g_base_url = "http://cdn.echo.msk.ru/snd"
g_episode_time_shifts = (0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5)


def get_last_program_time(pr, now_time=datetime.datetime.now()):
    threshold = now_time - config.publishing_delay
    the_time = datetime.datetime(threshold.year, threshold.month, threshold.day, pr["time"].hour, pr["time"].minute)
    while the_time >= threshold or the_time.weekday() != pr["dow"].value:
        the_time -= datetime.timedelta(days=1)
    return the_time


def get_episode_path(pr, episode_name):
    return os.path.join(make_programme_folder(pr), episode_name)


def was_downloaded(pr, dt):
    return any([os.path.exists(get_episode_path(pr, ep)) for ep in possible_episode_file_names(pr, dt)])
    # for episode_name in possible_episode_file_names(pr, dt):
    #     return os.path.exists(get_episode_path(pr, episode_name))


def make_programme_folder(pr):
    folder_path = os.path.join(config.output_dir, pr["name"])
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def possible_episode_file_names(pr, dt):
    result = []
    for shift in g_episode_time_shifts:
        tt = datetime.time(pr["time"].hour, pr["time"].minute + shift)
        result.append(
            "{}-{}-{}.mp3".format(dt.strftime("%Y-%m-%d"), pr["code"], tt.strftime("%H%M"))
        )
    return result


def make_url(episode_name):
    return "{}/{}".format(g_base_url, episode_name)


def download(pr, dt):
    for episode_name in possible_episode_file_names(pr, dt):
        url = make_url(episode_name)
        ep_path = get_episode_path(pr, episode_name)
        try:
            with urlopen(url) as rr, open(ep_path, "wb") as ff:
                ff.write(rr.read())
                print("Episode {} downloaded.".format(episode_name))
                break
        except HTTPError:
            continue
    else:
        print("Can't download {} for {}. Maybe it's not published yet?".format(pr["name"], dt.strftime("%d.%m")))


if __name__ == '__main__':
    for pr in config.programmes:
        last_program_time = get_last_program_time(pr)
        if not was_downloaded(pr, last_program_time):
            download(pr, last_program_time)
        else:
            print("Episode {} for {} was ALREADY downloaded.".format(pr["name"], last_program_time.strftime("%d.%m")))
