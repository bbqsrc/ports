--- test.py.orig	2015-01-14 10:08:20 UTC
+++ test.py
@@ -5,6 +5,7 @@ import subprocess
 import os
 import shutil
 import time
+import sys
 
 
 def call(cmd):
@@ -51,7 +52,7 @@ class Common:
 		# if it fails for someone, let's find the race and fix it!
 		#time.sleep(1)
 
-		call('fusermount -u union')
+		call('umount union')
 
 		for d in self._dirs:
 			shutil.rmtree(d)
@@ -238,6 +239,7 @@ class IOCTL_TestCase(Common, unittest.Te
 		call('src/unionfs rw1=rw:ro1=ro union')
 	#enddef
 
+	@unittest.skipUnless(sys.platform.startswith('linux'), "Linux-only ioctl")
 	def test_debug(self):
 		# TODO: this is not safe, use some temporary filename or something
 		if os.path.exists('/tmp/test_debug.log'):
