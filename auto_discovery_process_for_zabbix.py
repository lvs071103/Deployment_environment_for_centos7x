#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# author: Jack.Z


import subprocess
import json


def get_puser_pname():
    command = "ps axo user:10,comm| grep Server"
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()
    stdout, stderr = result
    data = list()
    for line in stdout.split('\n'):
        result_list = [x for x in line.split(' ') if x != '']
        if result_list:
            data.append({"#{PUSER}": result_list[0], "{#PNAME}": result_list[1]})

    return json.dumps({"data": data})


if __name__ == "__main__":
    print get_puser_pname()
