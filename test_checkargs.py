import pytest
import checkargs

def test_checkargs():

    answers = open("answers.txt").read().split("\n")
    functions = []
    args = {}

    for ans in answers:
        # Skip comments
        if "#" in ans:
            continue
        tmp = ans.split(" ")
        func = tmp[0]
        arg = tuple(tmp[1:])
        functions.append(func)
        args[func] = arg
    
    source = open("kernels.cu").read()

    checkargs.checkargs(source, "add", args["add"])
    checkargs.checkargs(source, "add2", args["add2"])
    with pytest.raises(TypeError) : checkargs.checkargs(source, "toofew", args["toofew"], )
    with pytest.raises(TypeError) : checkargs.checkargs(source, "toomany", args["toomany"], )
    with pytest.raises(TypeError) : checkargs.checkargs(source, "block_toofew", args["block_toofew"], )
    with pytest.raises(TypeError) : checkargs.checkargs(source, "block_toomany", args["block_toomany"], )

