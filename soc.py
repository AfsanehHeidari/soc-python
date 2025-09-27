class Soc:
    def __init__(self):
        self.reset()

    def reset(self):
        self.registers = {
            0X00: 0X0,
            0x04: 0x1
       }
    
    def write(self, addr: int, data: int):
        if addr == 0x00:
            self.registers[addr] = data
            self.registers[0x04] = 1 if (data %2 == 0) else 0
        else:
            raise ValueError(f"Write to invalid  addr 0x{addr: X}")

    def read(self, addr: int) -> int:
        if addr in self.registers:
            return self.registers[addr]
        else:
            raise ValueError(f"Read fron invalid addr 0x{addr: X}")