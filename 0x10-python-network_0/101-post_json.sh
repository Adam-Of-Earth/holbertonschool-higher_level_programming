#!/bin/bash
#post a json file
curl -sH 'Content-Type: application/json' -d "@$2" "$1"