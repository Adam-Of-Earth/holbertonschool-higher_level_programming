#!/bin/bash
# sends a url request
curl -sI "$1" | grep 'Content-Length' | cut -d ' ' -f 2
