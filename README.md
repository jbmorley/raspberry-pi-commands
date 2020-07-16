# raspberry-pi-commands

Simple script to monitor Raspberry Pi GPIO pins and run commands

## Usage

To add a shutdown button by running `raspberry-pi-commands.py` on reboot, adding the following to your crontab:

```bash
@reboot /usr/bin/python3 \
	/home/pi/Projects/raspberry-pi-commands/raspberry-pi-commands.py \
	--pin 21 --command "sync; sudo shutdown"
```
