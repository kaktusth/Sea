"""
The following are Excitation classes encapsulating their respective Sea.model.excitations class.
"""


import logging

import Sea
import baseclasses

class ExcitationPoint(baseclasses.Excitation):
    """
    Rain on the roof excitation
    """

    name = 'Point'
    description = 'An excitation of a single point.'
    
    model = Sea.model.ExcitationPoint()
    
    def __init__(self, obj, system, subsystem, **properties):
        baseclasses.Excitation.__init__(self, obj, system, subsystem, **properties)
        
        
        
        
class ExcitationRain(baseclasses.Excitation):
    """
    Rain on the roof excitation
    """

    name = 'Rain'
    description = 'An excitation averaged over space and time.'
    
    model = Sea.model.ExcitationRain()
    
    def __init__(self, obj, system, subsystem, **properties):
        baseclasses.Excitation.__init__(self, obj, system, subsystem, **properties)
        
        
        
        
        
        
        

import inspect, sys
excitations_map = {item[0]: item[1] for item in inspect.getmembers(sys.modules[__name__], inspect.isclass)}
"""
Dictionary with all available excitations.
"""