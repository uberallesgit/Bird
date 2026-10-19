[app]

# (str) Title of your application
title = Сводка ЦТЭиСО

# (str) Package name
package.name = cteso_report

# (str) Package domain (needed for android/ios packaging)
package.domain = org.uber

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec, txt, md

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = venv, __pycache__, .git, .idea

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# openpyxl нужен для работы с Excel, kivy для интерфейса, et-xmlfile - зависимость openpyxl
requirements = python3,kivy==2.3.0,openpyxl,et-xmlfile

# (str) Presplash of the Application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the Application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# ВАЖНО: Разрешения на чтение и запись для доступа к папке Download на Android
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 24

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (str) Bootstrap to use (either sdl2, pygame or webview)
#android.bootstrap = sdl2

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add (currently works only with sdl2 bootstrap)
#android.add_aars =

# (list) Gradle dependencies to add (currently works only with sdl2 bootstrap)
#android.gradle_dependencies =

# (list) add java compile options
#android.add_compile_options = sourceCompatibility JavaVersion.VERSION_1_8, targetCompatibility JavaVersion.VERSION_1_8

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#ouya.category = APP

#
# iOS specific
#

#
# Python for android (p4a) specific
#

# (str) python-for-android fork to use, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the pip requirements file for your application
#p4a.pip_options =

#
# Cython direct build
#

#
# Windows specific
#

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1