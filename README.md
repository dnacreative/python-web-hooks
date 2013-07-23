python-web-hooks
================

Trying hooks into online, free systems: automated tests and builds (travis), export github to read-the-docs, auto-deploy, etc

#### Generating Documentation

Auto-generate api docs

```
sphinx-apidoc -o doc/source web_hooks # -f to overwrite
```

make HTML (from `docs/` path, where makefile resides)
 
```
make html
```