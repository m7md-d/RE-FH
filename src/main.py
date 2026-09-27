import lief
from get_function import get_function_code
from capstone0 import mc_decode

elf = lief.ELF.parse("code")
if elf is None:
    raise RuntimeError("Failed to parse the file")

address, code = get_function_code(elf, "main")

print(f"main @ {address:#x}")
print(code.hex(" "))

mc_decode(code, address)
