def analyze_opcodes(dex):
    opcodes = {}
    for method in dex.get_methods():
        bytecode = method.get_code()
        if bytecode:
            for instruction in bytecode.get_bc().get_instructions():
                op_name = instruction.get_name()
                opcodes[op_name] = opcodes.get(op_name, 0) + 1
    return opcodes
