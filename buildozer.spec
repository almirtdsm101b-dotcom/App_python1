[app]

# (str) Title of your application
title = Meu App Teste

# (str) Package name
package.name = appteste

# (str) Package domain (needed for android packaging)
package.domain = org.almir

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Specify 'python3', 'kivy'
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET
