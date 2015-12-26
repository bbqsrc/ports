--- src/unionfs.c.orig	2015-01-14 10:08:20 UTC
+++ src/unionfs.c
@@ -92,7 +92,11 @@ static int unionfs_chmod(const char *pat
 	char p[PATHLEN_MAX];
 	if (BUILD_PATH(p, uopt.branches[i].path, path)) RETURN(-ENAMETOOLONG);
 
+#if __FreeBSD__
+	int res = lchmod(p, mode);
+#else
 	int res = chmod(p, mode);
+#endif
 	if (res == -1) RETURN(-errno);
 
 	RETURN(0);
@@ -287,6 +291,7 @@ static int unionfs_ioctl(const char *pat
 			return -EINVAL;
 		return 0;
 	}
+#ifndef __FreeBSD__
 	case UNIONFS_SET_DEBUG_FILE: {
 		char *debug_path = (char *) data;
 
@@ -295,6 +300,7 @@ static int unionfs_ioctl(const char *pat
 		debug_init();
 		return 0;
 	}
+#endif
 	default:
 		USYSLOG(LOG_ERR, "Unknown ioctl: %d", cmd);
 		return -EINVAL;
