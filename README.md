# raspberry-pi-shutdown

Simple script to monitor Raspberry Pi GPIO pins for shutdown command

## Usage

Add the script to crontab. For example,

```bash
@reboot /usr/bin/sudo /usr/bin/python3 /home/pi/Projects/raspberry-pi-shutdown/raspberry-pi-shutdown.py
```

