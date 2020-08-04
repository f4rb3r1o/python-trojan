# python-trojan

very simple project.

Client running as an agent on a target machine, has only two capabilities:

1. sending a file up to the C2
2. getting a file from the C2 and loading it as a dynamic library (depends on the target platform).

server is single threaded
