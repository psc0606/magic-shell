#!/bin/env python2
# coding=utf-8
import os

"""
Just used by to clean storm logs, can use cron to schedule this script.
"""


def get_storm_logs_dir(path):
    dirs = os.listdir(path)
    storm_jobs = {}
    for d in dirs:
        if not os.path.isdir(d):
            continue
        storm_job_name, job_start_time = split_name_and_time(d)

        # 仅保留时间戳最近的任务
        if storm_job_name not in storm_jobs:
            storm_jobs[storm_job_name] = d
        elif storm_job_name in storm_jobs:
            old = storm_jobs[storm_job_name]
            if split_name_and_time(old)[1] < job_start_time:
                storm_jobs[storm_job_name] = d

    print '保留:'
    print storm_jobs.values()
    to_deleted_dirs = [i for i in dirs if i not in storm_jobs.values()]
    for d in to_deleted_dirs:
        # 仅删目录
        if os.path.isdir(d):
            print '删除目录:%s' % d
            cmd = 'rm -fr ' + d
            os.system(cmd)
            # os.removedirs(d)


def split_name_and_time(path):
    storm_job_name = '-'.join(path.split('-')[:-2])
    job_start_time = int(path.split('-')[-1])
    return storm_job_name, job_start_time


def do_clean():
    LOG_PATH = '/tmp/soft/apache-storm-1.1.0/logs/workers-artifacts'
    print os.getcwd()
    if os.getcwd() == LOG_PATH:
        get_storm_logs_dir('.')
        return
    print '不在%s' % LOG_PATH


if __name__ == '__main__':
    do_clean()
