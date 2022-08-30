class Control:
    
    def __init__ (self):
        self._tv = None

    def getTv (self):
        return self._tv

    def setTv (self, tv):
        self._tv = tv

    def enlazar (self, tv):
        self.setTv(tv)
        self._tv.setControl(self)

    def turnOff (self):
        self._tv.turnOff()
    
    def turnOn (self):
        self._tv.turnOn()
    
    def volumenUp (self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()
    
    def canalUp (self):
        self._tv.canalUp()
        
    def canalDown (self):
        self._tv.canalDown()

    def getCanal (self):
        return self._tv.getCanal()
    
    def setCanal (self,cambio):
        self._tv.setCanal(cambio)