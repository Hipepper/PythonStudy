import dis

# print(dis.opname)
# print(dis.opmap)
# s_code = '1 and 1'
# c = compile(s_code, '', 'eval')
# print(c.co_code)
# print(c.co_names)
# print(c.co_consts)
# # print(c.co_code.hex())
# dis.dis(s_code)
# dis.dis("__import__('os').system('dir')")
# dis.dis("1 and 1")

s_code = "__import__('os').system('dir')"
s_code = "__import__('builtins').open('/bin/ls', 'r')"
s_code = "1 and (1 + 1) or 0"
s_code = "'testtesttest'.startwith('test')"
# s_code = "min(1,0)"
c = compile(s_code, '', 'eval')
print(c.co_code)

import sys
def disassemble(co, b_ret_code=False):
    opcode = []
    if sys.version_info.major != 3:
        return opcode
    if sys.version_info.minor < 4:
        if isinstance(co, str):
            code = compile(co, '', 'eval').co_code
        else:
            code = co.co_code
        n = len(code)
        i = 0
        while i < n:
            op = code[i]
            if b_ret_code:
                opcode.append(op)
            else:
                opcode.append(dis.opname[op])
            i = i + 1
            if op >= dis.HAVE_ARGUMENT:
                i = i + 2
    else:
        bytecode = dis.Bytecode(co)
        for instr in bytecode:
            if b_ret_code:
                opcode.append(instr.opcode)
            else:
                opcode.append(instr.opname)
    return opcode

opcode = disassemble(s_code, True)
print(opcode)

opcode = disassemble(s_code)
print(opcode)

opcode = disassemble(c, True)
print(opcode)

opcode = disassemble(c)
print(opcode)

