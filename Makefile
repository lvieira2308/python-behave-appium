.PHONY: android-tests ios-tests

android-tests:
	behave -D PLATFORM=android

ios-tests:
	behave -D PLATFORM=ios
