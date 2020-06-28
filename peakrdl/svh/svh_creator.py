############################################################################
# Main svh creater class with required properties
# for creating the svh contents and adding the data 
# into the svh file(s)
############################################################################
class svhCreator:

    def __init__(self, output_file: str, **kwargs):
        """
        Constructor for the svh Creator class
        """

        # Check for stray kwargs
        if kwargs:
            raise TypeError("got an unexpected keyword argument '%s'" % list(kwargs.keys())[0])
