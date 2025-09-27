from soc import Soc
from random import randint

CTRL_ADDR = 0X00
STATUSE_ADDR = 0X04

dut = Soc()

print("=== Test Start ===")

dut.reset()
assert dut.read(0X00) == 0x0, "CTRL reset mismatch"
assert dut.read(0x04) == 0x1, "STATUS reset mismatch"
print("Reset passed")

dut.write(0x00, 4)
assert dut.read(0x00) == 4, "CTRL write/read mismatch"
assert dut.read(0x04) == 1, "STATUS side effect failed(expected even number)"
print("CTRL=4 -> STATUS=1 OK")

dut.write(0x00, 5)
assert dut.read(0x00) == 5, "CTRL write/read mismatch"
assert dut.read(0x04) == 0, "STATUS side effect failed(expected odd number)"
print("CTRL=5 -> STATUS=0 OK")

for _ in range(10):
    val = randint(0, 255)
    dut.write(CTRL_ADDR, val)
    ctrl= dut.read(CTRL_ADDR)
    status = dut.read(STATUSE_ADDR)
    assert ctrl == val, f"CTRL mismatch: wrote {val}, read {ctrl}"
    assert status == (val % 2 == 0), f"STATUS mismatch for CTRL={val}"
print("Randomized tests OK")

print("Register Read/Write test PASSED")
