#!/bin/bash
# Super quick test - results in ~90 seconds

echo "⚡ QUICK TEST - 90 seconds total"
echo "================================"

echo "1. Starting & killing shellhorn..."
shellhorn sleep 180 &
PID=$!
sleep 2
kill -9 $PID
pkill -9 -f "shellhorn.*sleep" || true
pkill -9 -f "sleep.*180" || true
echo "   ✅ Shellhorn killed (timeout: 30s)"

echo ""
echo "2. ⏰ Waiting 90 seconds for detection..."
for i in {90..1}; do
    printf "\r   ⏳ %02ds remaining" $i
    sleep 1
done

echo ""
echo ""
echo "🎯 Check monitor logs now - should show Pushover alert!"
echo "   docker logs shellhorn-monitor-dev --tail=10"