#!/bin/bash
#sends a request to be passed an argument
curl -s -o /dev/null -w %{http_code} "$1"
