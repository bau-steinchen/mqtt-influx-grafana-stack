#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 {start|stop|status}"
    exit 1
fi

case "$1" in
    start)
        echo "Start mqtt-influx-grafana stack..."
        docker-compose up -d --build --platform linux/arm/v7
        ;;
    stop)
        echo "Stop mqtt-influx-grafana stack..."
        docker-compose down
        ;;
    status)
        echo "Status for mqtt-influx-grafana stack:"
        docker-compose ps
        ;;
    *)
        echo "Illegal parameter! Usage: $0 {start|stop|status}"
        exit 1
        ;;
esac
