#####################################################################
#                                 DOC                               #
#####################################################################

"""
@author: F. Ramognino       <federico.ramognino@polimi.it>
Last update:        12/06/2023
"""

#####################################################################
#                               IMPORT                              #
#####################################################################

from libICEpost.src.base.BaseClass import BaseClass, abstractmethod


from collections.abc import Iterable
import numpy as np
import pandas as pd

#############################################################################
#                               MAIN CLASSES                                #
#############################################################################
class EngineGeometry(BaseClass):
    """
    Base class for handling engine geometrical parameters during cycle.
    
    NOTE: Crank angles are defined with 0 CAD at TDC
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Attibutes:
        
    """
    
    
    #########################################################################
    def __str__(self):
        STR =  "{:15s} {:15s}".format("TypeName", self.TypeName)
        
        return STR
    
    ###################################
    #Instant. chamber volume:
    @abstractmethod
    def V(self,CA:float|Iterable) -> float|np.ndarray:
        """
        Returns the instantaneous in-cylinder volume at CA

        Args:
            CA (float | Iterable): Time in CA

        Returns:
            float|np.ndarray[float]: In-cylinder volume [m^3]
        """
        pass
    
    ###################################
    @abstractmethod
    def A(self,CA:float|Iterable) -> float|np.ndarray:
        """
        Returns the chamber area at CA
        Args:
            CA (float | Iterable): Time in CA

        Returns:
            float|np.ndarray[float]: [m^2]
        """
        pass
    
    ###################################
    @abstractmethod
    def areas(self,CA:float|Iterable) -> pd.DataFrame:
        """
        CA:     float / list<float/int>
            Crank angle
        
        Returns a pandas.Dataframe with area of all patches at CA
        """
        pass
    
    ###################################
    #Time (in CA) derivative of chamber volume:
    @abstractmethod
    def dVdCA(self,CA:float|Iterable) -> float|np.ndarray:
        """
        Returns the time (in CA) derivative of instantaneous in-cylinder volume at CA
        Args:
            CA (float | Iterable): Time in CA

        Returns:
            float|np.ndarray[float]: dV/dCA [m^3/CA]
        """
        pass
    
    
#########################################################################
#Create selection table
EngineGeometry.createRuntimeSelectionTable()