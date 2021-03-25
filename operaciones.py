class operaciones:

    def _init_(self):
        self.val1 = 0
        self.val2 = 0
        self.res = 0

    def suma(self):
        self.res = self.val1 + self.val2
        print('El resultado es: '+str(self.res))
        return self.res
    
    def resta(self):
        self.res = self.val1 - self.val2
        print('El resultado es: '+str(self.res))
        return self.res

    def multiplicacion(self):
        self.res = self.val1 * self.val2
        print('El resultado es: '+str(self.res))
        return self.res

    

        
