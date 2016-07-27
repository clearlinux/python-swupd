#!/bin/bash

fileset=`find swupd/ -name '*.py'`
pep8 $fileset || exit 1
flake8 $fileset || exit 1

