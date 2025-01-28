.PHONY: android-tests ios-tests

android-tests:
	pkill -f "appium" || true
	appium -p 4725 --use-plugins=images,appium-reporter-plugin > appium.log 2>&1 &
	sleep 5
	behave -D PLATFORM=android
	pkill -f "appium" || true

ios-tests:
	pkill -f "appium" || true
	appium -p 4724 --use-plugins=images,appium-reporter-plugin > appium.log 2>&1 &
	sleep 5
	behave -D PLATFORM=ios
	pkill -f "appium" || true
