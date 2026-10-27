[app]
title = NetLink2nd
package.name = netlink2nd
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Финальная правка: фиксируем версии пакетов
requirements = python3,kivy,pyjnius>=1.4.0,charset_normalizer==2.1.1

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.archs = arm64-v8a
android.accept_sdk_license = True

p4a.branch = master
android.clear_cache = 1

[buildozer]
log_level = 2
warn_on_root = 0
