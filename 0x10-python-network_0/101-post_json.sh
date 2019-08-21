#!/bin/bash
#post a json file
curl -s 'Content-Type: application/json' -d "@${2}" "$1"
