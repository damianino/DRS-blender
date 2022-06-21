import os
import subprocess
import bpy



pythonBinaryPath = os.path.join(bpy.utils.user_resource('CONFIG')[:-6], "python", "bin", "python.exe")

res = subprocess.call([pythonBinaryPath, "-m",  "pip", "install", "--upgrade", "pip"] )
res = subprocess.call([pythonBinaryPath, "-m",  "pip", "install", "-Iv", "--upgrade", "protobuf"] )
res = subprocess.call([pythonBinaryPath, "-m",  "pip", "install", "-Iv", "--upgrade", "grpcio"] )
res = subprocess.call([pythonBinaryPath, "-m",  "pip", "install", "-Iv", "--upgrade", "grpcio-tools"] )
res = subprocess.call([pythonBinaryPath, "-m",  "pip", "install", "-Iv", "--upgrade", "Pillow"] )

