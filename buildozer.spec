[app]
title = NetLink2nd
package.name = netlink2nd
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,jnius,libffi
orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 36
android.minapi = 24
android.ndk = 29
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

p4a.branch = develop
log_level = 2

[buildozer]
warn_on_root = 0
