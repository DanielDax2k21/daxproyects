[app]
title = Descargador de Videos
package.name = videodownloader
package.version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,yt-dlp,certifi,urllib3,idna,charset-normalizer,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = arm64-v8a
p4.branch = master
icon.filename = 
presplash.filename = 

[buildozer]
log_level = 2
warn_on_root = 1