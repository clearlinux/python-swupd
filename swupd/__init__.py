#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of python-swupd

# Copyright © 2016 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess
import urllib2
import os


def get_latest_version():
    url = 'https://download.clearlinux.org/update/version/formatstaging/latest'
    f = urllib2.urlopen(url)
    content = f.read().rstrip('\n')
    return content


def get_bundle_list(version):
    base_url = 'https://download.clearlinux.org/update/'
    MoM_url = base_url + str(version) + '/Manifest.MoM'
    bundle_list = []
    f = urllib2.urlopen(MoM_url)
    content = f.read().rstrip('\n')
    file_out = content.split('\n')
    for fo in file_out:
        l = fo.split('\t')
        if len(l) == 4:
            bundle_list.append(l[-1])
    return bundle_list


def get_installed_bundles():
    bundles_dir = '/usr/share/clear/bundles/'
    p = os.listdir(bundles_dir)
    return p


def install_bundles(bundle_list, F=None, url=None):
    latest_version = get_latest_version()
    installed_bundles = get_installed_bundles()
    bundle_universe = get_bundle_list(latest_version)
    exit_status = 0
    out = ""
    err_ = ""
    err = ""
    if len(bundle_list) == 0:
        err = "Bundle list was empty"
    for bundle in bundle_list:
        if(bundle in installed_bundles):
            err_ += "The bundle " + str(bundle)
            err_ += " is already installed"
            err = ""
            exit_status = 1
        else:
            cmd = ['sudo', 'swupd', 'bundle-add']
            if bundle in bundle_universe:
                cmd += [bundle]
                if F is not None:
                    cmd += ['-F', F]
                if url is not None:
                    cmd += ['-u', url]
                cmd += [bundle]
                p = subprocess.Popen(cmd,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
                o, e = p.communicate()
                out += o
                err += e
                if exit_status == 0:
                    exit_status = p.returncode
            else:
                err_ += "The bundle " + str(bundle)
                err_ += " does not exists on Clear Linux bundle universe"
                exit_status = 1
        err = str(err_) + str(err)
    return (out, err, exit_status)


def remove_bundles(bundle_list):
    installed_bundles = get_installed_bundles()
    exit_status = 0
    out = ""
    err = ""
    err_ = ""
    for bundle in bundle_list:
        if(bundle in installed_bundles):
            p = subprocess.Popen(['sudo', 'swupd', 'bundle-remove', bundle],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            o, e = p.communicate()
            out += o
            err += e
            if exit_status == 0:
                exit_status = p.returncode
        else:
            err_ += "The bundle " + str(bundle) + " is not installed"
            exit_status = 1
    err = str(err_) + str(err)
    return (out, err, exit_status)


def update():
    exit_status = 0
    out = ""
    err = ""
    p = subprocess.Popen(['sudo', 'swupd', 'update'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()
    exit_status = p.returncode
    return (out, err, exit_status)
