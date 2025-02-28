#!/bin/bash

set -euo pipefail

# DEBUG set in .env
if [ ${DEBUG:-0} = 1 ]; then
    log_level="DEBUG"
else
    log_level="INFO"
fi

# Wait for db migrations
sleep 10

echo "==> $(date +%H:%M:%S) ==> Running Celery beat <=="
exec celery -A config.celery_app beat -S django_celery_beat.schedulers:DatabaseScheduler --loglevel $log_level
