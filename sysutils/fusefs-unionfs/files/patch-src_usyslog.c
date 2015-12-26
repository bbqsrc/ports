--- src/usyslog.c.orig	2015-12-26 04:10:53 UTC
+++ src/usyslog.c
@@ -23,7 +23,7 @@
 
 #if __APPLE__
 #include <malloc/malloc.h>
-#else
+#elif !defined(__FreeBSD__)
 #include <malloc.h>
 #endif
 
