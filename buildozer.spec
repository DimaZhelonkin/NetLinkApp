[app]
title = NetLink2nd
package.name = netlink2nd
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pyjnius
orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

# Эти две строки заставляют сборщик использовать свежий код и не искать старые бинарники
p4a.branch = develop
android.clear_cache = 1

[buildozer]
log_level = 2
warn_on_root = 0
