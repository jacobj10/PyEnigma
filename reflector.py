class Reflector():
    def __init__(self):
        self.reflector_list=(9 , 10 , 2 , 14 , 15 , 13 , 11 , 12 , 16 , 
                            1 , 8 , 26 , 21 , 24 , 3 , 22 , 25 , 19 , 
                            4 , 6 , 7 , 17 , 23 , 5 , 18 , 20)
        self._dict = {}
        self.generate_reflect_dict()

    def generate_reflect_dict(self):
        x=0
        while x<len(self.reflector_list)-1:
            self._dict[chr(self.reflector_list[x]+64)]=chr(self.reflector_list[x+1]+64)
            self._dict[chr(self.reflector_list[x+1]+64)]=chr(self.reflector_list[x]+64)
            x+=2
        return self._dict
