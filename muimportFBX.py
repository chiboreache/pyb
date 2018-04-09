import os
import bpy
import glob

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
importDir = desktop + '\\fbx'

os.chdir(importDir)
for files in glob.glob('*.fbx'):
    bpy.ops.import_scene.fbx(filepath=files, filter_glob='*.fbx;', axis_forward='-Z', axis_up='Y')
