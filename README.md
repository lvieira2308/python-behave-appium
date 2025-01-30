# Setup

brew install carthage


brew install libimobiledevice
idevice_id -l           # - Lists your iOS device connected via USB
ideviceinfo             # - Lists all relevant info from your device
ideviceinfo | grep DeviceName


brew install ideviceinstaller
ideviceinstaller - l          # - Lists all apps (bundle ids) installed on your device

# Run commands

## First - Enter in the shell mode
poetry shell

## Second - Run tests using paver or make commands for the desired platform

paver run_tests android
paver run_tests ios

make run_tests_android
make run_tests_ios
