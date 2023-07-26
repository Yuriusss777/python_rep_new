class Phone:
    screen = 1
    def __init__(self, sims, plat):
        self.sims = sims
        self.plat = plat

    def call(self):
        pass


obj = Phone(2, 'android')
print(obj.sims)
obj.sims = 1
print(obj.sims)
obj.call()

