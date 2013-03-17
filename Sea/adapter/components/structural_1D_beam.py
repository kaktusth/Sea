"""
Adapter classes for :class:`Sea.model.components.Component1DBeam`
"""

import Sea
from .. import baseclasses

class Component1DBeam(baseclasses.ComponentStructural):
    """
    Beam structural component.
    """
    name = 'Beam'
    description = 'A structural component with wave propagation along one dimension.'
    
    model = Sea.model.components.Component1DBeam()
    """
    This adapter describes a :class:`Sea.model.components.Component1DBeam`
    """
    
    def __init__(self, obj, system, material, part):
        baseclasses.ComponentStructural.__init__(self, obj, system, material, part)
        

        obj.addProperty("App::PropertyLength", "Length", "Beam", "Length of the beam")
        obj.setEditorMode("MaxLength", 2)
        
        obj.addProperty("App::PropertyFloat", "CrossSection", "Beam", "Cross section of the beam")
        obj.setEditorMode("CrossSection", 2)
        
        obj.addProperty("App::PropertyFloat", "MassPerArea", "Beam", "Mass per unit area")
        obj.addProperty("App::PropertyFloat", "AreaMoment", "Beam", "Area moment of inertia")

 

         

    def onChanged(self, obj, prop):
        baseclasses.ComponentStructural.onChanged(self, obj, prop)
        
        if prop == 'Length':
            self.model.length = obj.Length
    
    def execute(self, obj):
        baseclasses.ComponentStructural.execute(self, obj)
        
        obj.Length = self.model.length
        obj.AreaMoment = self.model.area_moment_of_inertia
        obj.CrossSection = self.model.cross_section
        
    
 
   
        
    