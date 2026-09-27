import lief

def get_function_code(elf: lief.ELF.Binary, fname):
    symbol = elf.get_symbol(fname)

    if symbol is None:
        raise RuntimeError(f"The function: {fname} not found")
    if symbol.size == 0:
        raise RuntimeError(f"The size of function: {fname} not recognized")

    address = symbol.value


    code = bytes(elf.get_content_from_virtual_address(address, symbol.size))

    return address, code
