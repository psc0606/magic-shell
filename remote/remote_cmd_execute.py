#!/bin/env python
# coding=utf-8
import paramiko
import paramiko.agent
import sys


class RemoteCommandExecutor(object):
    @staticmethod
    def execute(user, host, port, cmd):
        """
        execute remote command
        :param user: user
        :param host: host
        :param port: ssh port
        :param cmd: command execute by remote
        """
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(
                hostname=host,
                port=port,
                username=user,
                look_for_keys=False,
                allow_agent=True,
                timeout=15,
                banner_timeout=15
            )
            stdin, stdout, stderr = client.exec_command(cmd)
            out = stdout.read().decode('utf-8')
            err = stderr.read().decode('utf-8')
            # cannot return stdin, stdout, stderr, because it was closed by client
            return out, err
        except KeyboardInterrupt:
            sys.exit(1)
        finally:
            client.close()
