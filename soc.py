class Soc:
    def __init__(self):
        self.reset()

    def reset(self):
        self.registers = {0X00: 0X0}
    
    def write(self, addr, data):
        self.registers[addr] = data

    def read(self, addr):
        return self.registers[addr]



class Soc:
    def __init__(self):
        self.reset()

    def reset(self):
        self.registers = {0x00: 0x0}

    def write(self, addr, data):
        self.registers[addr] =data

    def read(self, addr):
        return self.registers[addr]