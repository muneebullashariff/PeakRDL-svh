import sys
import os
import re
import datetime
import time

from systemrdl.node import RootNode, Node, RegNode, AddrmapNode, RegfileNode
from systemrdl.node import FieldNode, MemNode, AddressableNode
from systemrdl.rdltypes import AccessType, OnReadType, OnWriteType

from .svh_creator import svhCreator

class svhExporter:
    
    def __init__(self, **kwargs):
        """
        Constructor for the svh Exporter class
        """

        # Check for stray kwargs
        if kwargs:
            raise TypeError("got an unexpected keyword argument '%s'" % list(kwargs.keys())[0])

        # Define variables used during export

        # Top-level node
        self.top = None

        # Dictionary of group-like nodes (addrmap, regfile) and their bus
        # widths.
        # key = node path
        # value = max accesswidth/memwidth used in node's descendants
        self.bus_width_db = {}

        # Dictionary of root-level type definitions
        # key = definition type name
        # value = representative object
        #   components, this is the original_def (which can be None in some cases)
        self.namespace_db = {}

        # Used for making the instance name(s) in uppercase or lowercase
        self.export_as_package = True

        # Used for address width - Default 32bits
        self.address_width = 32 

        # Used for absoulte address calculations
        self.base_address = 0x0

        # Get the today's date (mm-dd-yyyy)
        self.today_date = datetime.date.today().strftime('%m-%d-%Y')

        # Get the current time (hh:mm:ss)
        self.current_time = time.strftime('%H:%M:%S') 

        # Create the global variable for svh creation
        global svh_create

    #####################################################################
    # Main function for initiating the exporting of svh files
    #####################################################################
    def export(self, node_list: list, path: str, **kwargs):
        """
        Perform the export!

        Parameters
        ----------
        node_list: List of systemrdl.Node(s)
            Top-level node to export. Can be the top-level `RootNode` or any
            internal `AddrmapNode`.

        path: str
            Output file.

        export_as_package: bool
            If True (Default), UVM register model is exported as a SystemVerilog
            package. Package name is based on the output file name.

            If False, register model is exported as an includable header.
        """

        self.export_as_package = kwargs.pop("export_as_package", True)

        # Check for stray kwargs
        if kwargs:
            raise TypeError("got an unexpected keyword argument '%s'" % list(kwargs.keys())[0])

        # Call the method for initiating the svh generation
        self.generate_output_svh(node_list, path)

        #if export_as_package:
        #    context['package_name'] = self.get_package_name(path)
        #    template = self.jj_env.get_template("top_pkg.sv")
        #else:
        #    context['include_guard'] = self.get_include_guard(path)
        #    template = self.jj_env.get_template("top_include.svh")
        #stream = template.stream(context)
        #stream.dump(path)

    #####################################################################
    # Generate the output svh files
    #####################################################################
    def generate_output_svh(self, root_list: list, path: str):
        pass
        ## Create the object
        #self.pdf_create = PDFCreator(path)

        ## Go through multiple input files 
        ## root_list is elaborated output of input .rdl file(s)
        #for root_id, root in enumerate(root_list):
        #    for node in root.descendants(in_post_order=True):

        #        # Traverse all the address maps
        #        if isinstance(node, AddrmapNode):
        #            self.create_regmap_list(node, root_id)
        #            self.create_regmap_registers_info(node, root_id)

        #    # Dump all the data into the pdf file 
        #    self.pdf_create.build_document()

    #####################################################################
    # 
    #####################################################################
    def get_package_name(self, path: str) -> str:
        s = os.path.splitext(os.path.basename(path))[0]
        s = re.sub(r'[^\w]', "_", s)
        return s

    #####################################################################
    # 
    #####################################################################
    def get_include_guard(self, path: str) -> str:
        s = os.path.basename(path)
        s = re.sub(r'[^\w]', "_", s).upper()
        return s

