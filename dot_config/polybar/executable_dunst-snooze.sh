#!/bin/sh

count=$(cat /tmp/notification_count)

case "$1" in
    --toggle)
        dunstctl set-paused toggle
        ;;
    *)
        if [ "$(dunstctl is-paused)" = "true" ]; then
            echo "DND"
        else
            echo "Notifications $count"
        fi
        ;;
esac
