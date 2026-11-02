[app]

# Título de tu aplicación
title = Descargador de Videos

# Nombre del paquete (sin espacios ni caracteres especiales)
package.name = videodownloader

# Dominio del paquete
package.domain = org.dax

# Directorio donde está el código fuente (el punto actual)
source.dir = .

# Extensiones de archivos a incluir en el empaquetado
source.include_exts = py,png,jpg,kv,atlas

# Versión de la aplicación
version = 0.1

# Dependencias de Python requeridas para Kivy y yt-dlp en Android
requirements = python3,kivy,yt-dlp,certifi,urllib3,idna,charset-normalizer,requests

# Orientación de la pantalla (portrait = vertical)
orientation = portrait

# Pantalla completa (0 = muestra la barra de estado de Android)
fullscreen = 0

# Permisos de Android necesarios para acceder a internet y guardar en almacenamiento
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Versiones de Android SDK y API (Configuradas a la API 33 para compatibilidad)
android.api = 33
android.minapi = 21
android.sdk = 33

# Aceptación automática de licencias de Android SDK en la nube de GitHub Actions
android.accept_sdk_license = True

# Arquitectura del procesador (arm64-v8a para móviles modernos)
android.archs = arm64-v8a

# Rama de Pyjnius por defecto
p4.branch = master

# Icono y pantalla de carga (vacíos por ahora para usar los predeterminados)
icon.filename = 
presplash.filename = 

[buildozer]

# Nivel de registro (2 = información detallada para depurar si falla)
log_level = 2

# Advertir si se ejecuta como root (1 = sí)
warn_root = 1