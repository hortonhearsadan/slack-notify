#! /bin/bash

while true
do
  if ! eval "$COMMAND";
    then curl -X POST -H 'Content-type: application/json' --data '{"text":"'"${MESSAGE}"'"}' "$SLACK_WEBHOOK"
    fi
  sleep "${PERIOD:-3600}"
done