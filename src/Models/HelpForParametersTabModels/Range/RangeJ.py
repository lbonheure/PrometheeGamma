from Models.HelpForParametersTabModels.Range.Range import Range

class RangeJ(Range):
    """
    A class to represent a range of incomparability threshold of PROMETHEE Gamma method

    Attributes
    ----------
    x : float
        min(gamma_ij, gamma_ji)
    y : float
        |gamma_ij - gamma_ji|
    Pmax : float
        maximum value of P, the preference parameter of PROMETHEE Gamma method
    Pmin : float
        minimum value of P, the preference parameter of PROMETHEE Gamma method

    Methods
    -------
    getValForP(P:float)
        return the incomparability threshold value for the value P of preference parameter
    setX(value:float)
        set the value of x
    setY(value:float)
        set the value of y
    setPmax(value:float)
        set the value of Pmax
    setPmin(value:float)
        set the value of Pmin
    """

    def __init__(self, x: float, y: float, Pmax:float, Pmin:float) -> None:
        """
        Parameters
        ----------
        x : float
            min(gamma_ij, gamma_ji)
        y : float
            |gamma_ij - gamma_ji|
        Pmax : float
            maximum value of P, the preference parameter of PROMETHEE Gamma method
        Pmin : float
            minimum value of P, the preference parameter of PROMETHEE Gamma method
        """
        self.x = x
        self.y = y
        self.Pmin = Pmin
        self.Pmax = Pmax
        valMin = self.x - self.y/self.Pmin
        valMax = self.x - self.y/self.Pmax
        super().__init__(valMin, valMax)


    def getValForP(self, P:float) -> float:
        """Return the indifference threshold value for the value P of preference parameter
        
        Return
        ------
        x - y/P : float
            min(gamma_ij, gamma_ji) - |gamma_ij - gamma_ji|/P
        """
        return self.x - self.y/P
    

    def setX(self, value:float):
        """Set the value of x
        
        Parameters
        ----------
        value : float
            the new value of x
        """
        self.x = value
        valMin = self.x - self.y/self.Pmin
        valMax = self.x - self.y/self.Pmax
        super().setMax(valMax)
        super().setMin(valMin)


    def setY(self, value:float):
        """Set the value of y
        
        Parameters
        ----------
        value : float
            the new value of y
        """
        self.y = value
        valMin = self.x - self.y/self.Pmin
        valMax = self.x - self.y/self.Pmax
        super().setMax(valMax)
        super().setMin(valMin)


    def setPmax(self, value:float):
        """Set the value of Pmax
        
        Parameters
        ----------
        value : float
            the new value of Pmax
        """
        self.Pmax = value
        valMin = self.x - self.y/self.Pmin
        super().setMin(valMin)


    def setPmin(self, value:float):
        """Set the value of Pmin
        
        Parameters
        ----------
        value : float
            the new value of Pmin
        """
        self.Pmin = value
        valMax = self.x - self.y/self.Pmax
        super().setMax(valMax)