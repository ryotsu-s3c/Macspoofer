#!/bin/bash
echo "Setting up you environment for using Macspoofer easily"

ifconfig wlan0 | grep ether | grep -oE [0-9abcdef:]{17} > mainmac.txt
sudo chmod +x macspoof.py

echo "Completed!!! Waring-Use insall.sh only when you when your mac address is default"
