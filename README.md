Network Protocol Dictionary
===

This is a YAML network protocol dictionary for all (binary based) OSI-Layer 1-4 protocols, eg. Ethernet, IP, TCP, UDP, etc.

- What this dictionary should be:
  - A complete **machine readable** *structure definition* dictionary for all binary based network protocols
  - Addon: some protocol documentation from wikipedia or RFCs for display use.
  - A reference for building a network packet from scratch in an application, mostly for applications dealing with network packets.

- What it is clearly **NOT**:
  - Currently: complete.
  - A replacement for reading RFCs: Dependencies and constraints are **NOT** defined in this dictionary
  - A source for implementing network stacks


How to add a new protocol
----

- Clone. 
- Install ruby+[kwalify](http://www.kuwata-lab.com/kwalify/) (gem install kwalify).
- Check structure-schema.yml.  
- Write protocol file in ./protocols/osi[layer]/[protocolname].yml. 
- Validate structure with 'kwalify -lf structure-schema.yml [path/to/protocolname].yml' or validate all at once with 'kwalify -lf structure-schema.yml ./protocols/osi*/*.yml'. 
- Set up a merge request.
- Be happy.

How to use this dictionary
----

Currently not recommended, because the project lacks deeper tests than just schema validation. ;)

- Clone. 
- Get a YAML library for your program language. Or get a converter for JSON or XML, to use these markup languages.
- Load desired protocol files, or all of them. 
- Use resulting data structures to build protocol packet structures.

This repository will provide examples or useable code snippets for specific programming languages in the future...
