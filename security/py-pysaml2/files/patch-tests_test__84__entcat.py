--- tests/test_84_entcat.py.orig	2015-12-23 21:20:13 UTC
+++ tests/test_84_entcat.py
@@ -72,7 +72,7 @@ def test_entcat_filter():
 
     mds = MetadataStore(ATTRCONV, sec_config,
                         disable_ssl_certificate_validation=True)
-    _path = "testfed-metadata.xml"
+    _path = full_path("testfed-metadata.xml")
     mds.imp(
         {"local": [_path]})
 
@@ -82,4 +82,4 @@ def test_entcat_filter():
 
 
 if __name__ == "__main__":
-    test_entcat_filter()
\ No newline at end of file
+    test_entcat_filter()
