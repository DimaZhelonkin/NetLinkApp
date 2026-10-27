[app]
# (str) Title of your application
title = NetLink2nd

# (str) Package name
package.name = netlink2nd

# (str) Package domain (needed for android package naming)
package.domain = org.test

# (str) Source code directory
source.dir = .

# (list) Source files to include (extensions)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 1.0

# (list) Application requirements
# Здесь мы жестко зафиксировали рабочую версию Python
requirements = python3==3.11.1,kivy,pyjnius

# (str) Supported orientations (valid options are: landscape, portrait, all)
orientation = portrait

# (int) Fullscreen mode, 0 or 1
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use
android.ndk_api = 24

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (bool) If True, then skip the license question
android.accept_sdk_license = True

# КРИТИЧЕСКИЙ ФЛАГ: Сбрасываем старый кэш хост-питона на сервере
android.clear_cache = 1

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
