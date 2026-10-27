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
android.api = 31
android.minapi = 21
# Изменили NDK на стабильный 23b и оставили только arm64 (современные телефоны)
android.ndk = 23b
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

p4a.branch = master
android.clear_cache = 1

[buildozer]
log_level = 2
warn_on_root = 0
