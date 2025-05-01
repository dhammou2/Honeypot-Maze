#!/bin/bash

WATCH_PATH="/home/user/SystemLogs"
FAKE_SCRIPT="/home/user/make_more_files.py"
REFRESH_INTERVAL=1

while true; do
    inotifywait -r -m -e access,open,modify,attrib "$WATCH_PATH" | while read path action file; do
        if [[ "$path" == *"sys_"* ]]; then
            echo "[!] Folder accessed: $path"
            python3 "$FAKE_SCRIPT" "$path"
        fi
    done &

    PID=$!
    sleep $REFRESH_INTERVAL
    kill $PID 2>/dev/null
done
