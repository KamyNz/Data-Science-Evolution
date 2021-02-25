#!/bin/bash

# setting directory to Documents
cd <PATH-OF-FOLDER-OF-TASKS>;
CURRENT="${PWD##*/}"

# running dirtree
/usr/local/bin/dirtree -o <PATH-OUT-FILE>/output_dirtree_$CURRENT.html **/*
