#!/usr/bin/env bash

PIPE=$(mktemp -u)
mkfifo $PIPE

exec 3<>$PIPE
rm $PIPE

trap "exec 3>&-" EXIT INT TERM

pacat --record --monitor-stream=0 \
    | sox -t raw --rate 44100 --encoding signed --endian little --bits 16 --channels 2 - -t dat - \
    | python transform.py >&3 &

while read -r line; do
    echo "$line"
done <&3 | glava --desktop --stdin --verbose
