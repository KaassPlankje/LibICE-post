#####################################################################
#                                 DOC                               #
#####################################################################

"""
@author: F. Ramognino       <federico.ramognino@polimi.it>
Last update:        12/06/2023

janaf7 thermodynamic propeties
"""

#####################################################################
#                               IMPORT                              #
#####################################################################

from libICEpost.src.base.Functions.runtimeWarning import fatalErrorInFunction
import json

import libICEpost.Database as Database
from libICEpost.Database import database

from libICEpost.src.thermophysicalModels.specie.specie import Molecule
Molecules = database.chemistry.specie.Molecules

constantCp_db = database.chemistry.thermo.Thermo.addFolder("constantCp")

#############################################################################
#                                   DATA                                    #
#############################################################################

#Define method to load from json dictionay
def fromJson(fileName, typeName="Molecules"):
    """
    Add constantCp type Thermo to the database from a json file. 
    Dictionaries containing either cp [J/kgK], cv [J/kgK], or 
    gamma of the mixture, and hf [J/kg] (optional).
    The specie must be already present in the molecule database
    (database.chemistry.specie.Molecules) and the name of its 
    dictionary consistent with it.

    Eg:
    {
        "Ar":
        {
            "gamma":1.666,
            "hf":0.0
        },

        "N2":
        {
            "cp":1036.8,
            "hf":0.0
        },

        "H2O":
        {
            "gamma":1.33,
            "hf":-13.42e6
        }
    }
    """
    from libICEpost.src.thermophysicalModels.specie.thermo.Thermo.constantCp import constantCp

    from libICEpost.Database import database
    from libICEpost.src.thermophysicalModels.specie.specie import Molecule
    Molecules = database.chemistry.specie.Molecules
    constantCp_db = database.chemistry.thermo.Thermo.constantCp
    
    try:
        with open(fileName) as f:
            data = json.load(f)
            for mol in data:
                Dict = {}
                for var in ["cp", "cv", "gamma", "hf"]:
                    if var in data[mol]:
                        Dict[var] = data[mol][var]
                    else:
                        Dict[var] = None

                constantCp_db[mol] = \
                    constantCp\
                        (
                            Molecules[mol].Rgas,
                            Dict["cp"],
                            Dict["cv"],
                            Dict["gamma"],
                            Dict["hf"]
                        )
                
    except BaseException as err:
        fatalErrorInFunction(fromJson,f"Failed to load the janaf7 database '{fileName}'", err)

#Load database
fileName = Database.location + "/data/constantCp.json"
fromJson(fileName)
del fileName

#Add method to database
constantCp_db.fromJson = fromJson