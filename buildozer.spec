[app]
title = NetLink2nd
package.name = netlink2nd
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,pyjnius==1.6.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25c
android.ndk_api = 24
android.archs = arm64-v8a
android.accept_sdk_license = True
android.clear_cache = 1

[buildozer]
log_level = 2
warn_on_root = 0
