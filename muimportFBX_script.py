import os
import bpy
import glob

os.chdir(os.path.join(os.environ['USERPROFILE'], 'Desktop', 'fbx'))

for files in glob.glob('*.fbx'):
	bpy.ops.import_scene.fbx(filepath=files, filter_glob='*.fbx;')
