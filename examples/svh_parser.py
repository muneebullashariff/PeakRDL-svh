import sys
import os
from systemrdl import RDLCompiler, RDLCompileError
from systemrdl.node import RootNode, Node, RegNode, AddrmapNode, RegfileNode
from systemrdl.node import FieldNode, MemNode, AddressableNode
from peakrdl.svh import svhExporter

# Ignore this. Only needed for this example
this_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(this_dir, "../input_files"))

input_dir = this_dir + "/input_files/"
output_dir = this_dir + "/output_files/"

# Get the input .rdl file from the command line
input_files = sys.argv[1:]

## Compile and elaborate the input .rdl file
rdlc = RDLCompiler()

## List for storing the elaborated ouput of each .rdl file
rdlc_elab_list = []

## Compile and store the elaborated object
try:
    for input_file in input_files:
        input_file = input_dir + input_file 
        rdlc.compile_file(input_file)
        rdlc_elab_list.append(rdlc.elaborate())

except RDLCompileError:
    sys.exit(1)

## Generate the PDF output files
exporter = svhExporter()

package_file_name = "example_register_defines_pkg.svh"

## Derive the output file(s) name
output_files = []
for in_fl in input_files:
    var_out = in_fl.replace(".rdl","_defines.svh")
    strg = os.path.join(output_dir, var_out)
    output_files.append(strg)

output_pkg_name = os.path.join(output_dir, package_file_name)

# Call the exporter
exporter.export(rdlc_elab_list, 
                output_files,
                output_pkg_name,
                export_as_package=True)

print("Successfully generated the output svh files")
