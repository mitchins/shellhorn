#!/usr/bin/env python3
"""
Test script for Shellhorn Monitor notifications
"""
import sys
import os
sys.path.append(os.path.dirname(__file__))

from shellhorn_monitor import ShellhornMonitor, ActiveCommand, load_config
from datetime import datetime

def test_notifications():
    """Test different notification types"""
    config = load_config()
    monitor = ShellhornMonitor(config)
    
    # Create a test command
    test_command = ActiveCommand(
        command="test -f /some/file.txt",
        client_id="test_client_123",
        start_time=datetime.now(),
        pid=12345
    )
    
    print("Testing notification system...")
    print(f"Config loaded: {config['notifications']}")
    
    # Test each notification type
    notification_types = ['start', 'success', 'fail', 'lost']
    
    for event_type in notification_types:
        enabled = config['notifications']['enabled_events'].get(event_type, False)
        print(f"\n{event_type.upper()} notifications: {'ENABLED' if enabled else 'DISABLED'}")
        
        if enabled:
            print(f"  Priority: {config['notifications']['pushover']['priority'].get(event_type, 0)}")
            print(f"  Message template: {config['notifications']['pushover']['messages'].get(event_type)}")
            
            # Uncomment to actually send test notification
            # monitor.send_event_notification(test_command, event_type)

if __name__ == "__main__":
    test_notifications()