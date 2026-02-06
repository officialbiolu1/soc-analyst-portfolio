#!/bin/bash

# failed_login_counter.sh
# Counts failed SSH login attempts from auth.log
# Usage: ./failed_login_counter.sh

LOG_FILE="/var/log/auth.log"

if [ ! -f "$LOG_FILE" ]; then
  echo "Log file not found: $LOG_FILE"
  exit 1
fi

COUNT=$(grep -c "Failed password" "$LOG_FILE")

echo "Failed SSH login attempts: $COUNT"
