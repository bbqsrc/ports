--- setup.py.orig	2015-12-23 21:36:18 UTC
+++ setup.py
@@ -169,7 +169,7 @@ class build_clib(_build_clib):
         # Ensure our temporary build directory exists
         try:
             os.makedirs(build_temp)
-        except IOError:
+        except (IOError, OSError):
             pass
 
         # Ensure all of our executanle files have their permission set
