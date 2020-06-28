# PeakRDL-svh
Used for creating the systemverilog header files, which contains the defines for the registers

## Install from Github using pip
mkdir path_to_folder  
cd path_to_folder  
git clone https://github.com/muneebullashariff/PeakRDL-svh.git  
cd to PeakRDL-svh   
pip install -e .      


Advantages of this approach are:  
1 - You can install package in your home projects directory.   
2 - Package includes .git dir, so it's regular Git repository. You can push to your fork right away.    

--------------------------------------------------------------------------------

## Exporter Usage
Pass the elaborated output of the [SystemRDL Compiler](https://github.com/muneebullashariff/systemrdl-compiler)
to the exporter.

```python
import sys
from systemrdl import RDLCompiler, RDLCompileError
from peakrdl.svh import svhExporter

rdlc = RDLCompiler()

try:
    rdlc.compile_file("path/to/my.rdl")
    root = rdlc.elaborate()
except RDLCompileError:
    sys.exit(1)

exporter = svhExporter()
exporter.export(root, "test.svh")
```
--------------------------------------------------------------------------------

## Reference

### `svhExporter.export(node, path, **kwargs)`
Perform the export!

**Parameters**

* `node`
    * Top-level node to export. Can be the top-level `RootNode` or any internal `AddrmapNode`.
* `path`
    * Output file.

**Optional Parameters**

* `export_as_package`
    * If True (Default), .svh files are exported as a SystemVerilog
      package. Package name is based on the output file name.
    * If False, .svh files are exported as an includable header.
