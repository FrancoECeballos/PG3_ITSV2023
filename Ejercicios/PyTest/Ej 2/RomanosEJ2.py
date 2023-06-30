class Roman():
    def roman_to_decimal(self,inp):
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(inp)):
            if i > 0 and rom[inp[i]] > rom[inp[i - 1]]:
                num += rom[inp[i]] - 2 * rom[inp[i - 1]]
            else:
                num += rom[inp[i]]
        return num