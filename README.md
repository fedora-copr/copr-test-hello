# rpkg-util v2+ friendly package

This package builds correctly both with rpkg-util v2 (Fedora <= 34) and
rpkg-util v3 (Fedora >= 35).

Warning warning, if you depend on `auto_pack = True` functionality, stop.
Rpkg-util v3 doesn't provide that functionality anymore and you have to use the
'{{{ }}}'-syntax templates.
