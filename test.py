from soc import Soc
dut = Soc()

print("=== Test Start ===")

dut.reset()
assert dut.read(0X00) == 0x0
print("Reset passed")

dut.write(0x00, 5)
assert dut.read(0x00) == 5
print("Write=5 -> Read=5 OK")

print("Test PASSED")
