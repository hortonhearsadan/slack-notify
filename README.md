# slack-notify

Send slack messages to channel if shell command returns falsey value.

image supports docker commands to run execs in other containers

```
services
  slack-notify:
    image: hortonhearsadan/slack-notify:latest
    container_name: vpn-notify
    environment:
      - COMMAND=ls -l
      - PERIOD=600
      - SLACK_WEBHOOK=xxxxxx
      - MESSAGE=stuffs broken
    # if docker command, mount the socket as a volume
#    volumes:
#      - '/var/run/docker.sock:/var/run/docker.sock:ro'
 ```
