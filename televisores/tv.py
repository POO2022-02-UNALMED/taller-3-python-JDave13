class TV:

    numTV = 0

    def __init__ (self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        TV.numTV += 1

    def setMarca (self,marca):
        self._marca = marca
    
    def getMarca (self):
        return self._marca

    def setControl (self,control):
        self.control = control
    
    def getControl (self):
        return self.control
    
    def setVolumen (self,volumen):
        if self.getEstado():
            self._volumen = volumen
    
    def getVolumen (self):
        return self._volumen
    
    def setPrecio (self,precio):
        self._precio = precio
    
    def getPrecio (self):
        return self._precio

    def setCanal (self, canal):
        if self.getEstado():
            if (canal>=1 and canal<=120):
                self._canal = canal
    
    def getCanal (self):
        return self._canal


    def turnOn (self):
        if self._estado == False:
            self._estado = True

    def turnOff (self):
        if self._estado == True:
            self._estado = False

    def getEstado (self):
        return self._estado
    
    def volumenUp (self):
        if (self.getEstado() == True and self.getVolumen() < 7):
            self._volumen += 1

    def volumenDown (self):
        if (self.getEstado() == True and self.getVolumen() > 0):
            self._volumen -= 1

    def canalUp (self):
        if (self.getEstado() == True):
            if (self.getCanal() < 120):
                self._canal += 1
            
    def canalDown (self): 
        if (self.getEstado() ): 
            if (self.getCanal() > 1):
                self._canal -= 1
    def setNumTV (num):
        TV.numTV =  num
    
    def getNumTV ():
        return TV.numTV