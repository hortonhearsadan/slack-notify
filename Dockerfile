FROM alpine:latest
RUN apk add --no-cache bash
RUN apk add --update docker openrc curl


LABEL maintainer="Daniel Horton"

COPY ./ /app/

WORKDIR /app


CMD /bin/bash main.sh