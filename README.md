# res-switcharoo
A small, simple utility that enables one to use a screen resolution that is otherwise not allowed. USE AT OWN RISK IF RUNNING ON OWN MACHINE.

This utility essentially automates a call to xrandr to set a screen resolution that is not natively supported on a display that has an arbitrary maximum (i.e. run your 768p display at 1080p if desired.) It will feature aspect ratio calculation in order to filter out which modes a user can safely select.

At this time, 16:9 ratio resolutions are the only ratios supported. More will be added in the near future.
