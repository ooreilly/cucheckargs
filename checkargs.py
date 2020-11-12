import re

def checkargs(source : str, function : str, args : tuple):
    """
    Check that number and types of arguments match kernel function signature.

    Args:
        source: Source code to extract function from.
        function: Name of the function to extract.
        args: A tuple of arguments to pass to the function.

    Raises:
        TypeError if the argument number is incorrect or if the function name cannot be found.

    """
    #TODO: Add support for type checking

    # Get CUDA kernel function signature
    regex = r'extern\s+"C"\s+__global__\s+void\s+%s\s*\(([\w\W]+?)\)' % function
    pattern = re.compile(regex, re.MULTILINE)
    match = re.findall(pattern, source)

    if not match:
        raise TypeError("Unable to parse: %s " % function)
    params = match[0].split(",")
    
    if len(params) != len(args):
        msg = "%s takes %d positional arguments but %d were given." % (function,
                len(params), len(args))
        raise TypeError(msg)
