#!/bin/bash
#sends a request to be passed an argument
curl -so /dev/null -w %{http_code} "$1"
