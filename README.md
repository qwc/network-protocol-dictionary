Network Protocol Dictionary
===

This is a YAML network protocol dictionary for all (binary based) OSI-Layer 1-4 protocols, eg. Ethernet, IP, TCP, UDP, etc.

The list may not be complete, if you're missing a protocol, just add it! 

How to add a new protocol
----

Clone. Check structure-schema.yml. Install kwalify (has ruby as dependency!). Write protocol file in ./protocols/osi[layer]/[protocolname].yml. Validate structure with 'kwalify -lf structure-schema.yml [path/to/protocolname].yml' or validate all at once with 'kwalify -lf structure-schema.yml ./protocols/osi*/*.yml'. Be happy.

How to use this dictionary
----

Clone. Get a YAML library for your program language. Load desired protocol files, or all of them. Use resulting data structures to build protocol packet structures.

This repository will provide examples or useable code snippets for specific programming languages in the future...