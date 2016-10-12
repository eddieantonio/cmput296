#!/bin/bash

# Copyright 2016 Eddie Antonio Santos.
# Derived from David Winterbottom's blog post:
# http://codeinthehole.com/writing/tips-for-using-a-git-pre-commit-hook/

make && git add ./*.html
RESULT=$?

[ $RESULT -ne 0 ] && exit 1
exit 0
