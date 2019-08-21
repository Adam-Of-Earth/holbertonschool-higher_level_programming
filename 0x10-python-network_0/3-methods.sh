#!/bin/bash
# list methods on remote
curl -Is "$@" | grep 'Allow' | cut -d ' ' -f 2-
