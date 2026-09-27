from capstone import Cs, CS_ARCH_X86, CS_MODE_64

decoder = Cs(CS_ARCH_X86, CS_MODE_64)
def mc_decode(code, adr):
    for ins in decoder.disasm(code, adr):
        print(
            f"{ins.address:#x}: "
            f"{ins.bytes.hex(' '):<24} "
            f"{ins.mnemonic:<8} "
            f"{ins.op_str}"
        )