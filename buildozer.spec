[app]
title = Rocketcalc
package.name = rocketcalc
package.domain = org.example.rocketcalc
version = 0.1

source.dir = .
source.include_exts = py,png,jpg,kv

requirements = python3,kivy

orientation = portrait

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.target = 33
android.archs = arm64-v8a,armeabi-v7a

# Entry point
entrypoint = main.py

[buildozer]
log_level = 2
