class Ex:
    value = '42 results for head first python '

    def test(self):
        self.value = '39 Lathom Road'

    def print_v(self):
        # self.value = 'Welcome to Pythong'
        print(self.value)

    def no_of_results(self):
        s = int(self.value.split(" ")[0])
        l = [i for i in range(1, s, 2)]
        print(l)


e = Ex()
print(Ex.__dict__)
e.print_v()
e.no_of_results()
