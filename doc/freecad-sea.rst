.. _freecad-sea:

SEA in FreeCAD
###############

.. toctree::
   :maxdepth: 2
   
The previous chapter explained what Statistical Energy Analysis is. 
In this chapter we will have a closer look on how SEA is implemented in FreeCAD-SEA.

=========
Overview
=========

An SEA model in FreeCAD-SEA is represented by the descendents of the following abstract objects

* :class:`Sea.adapter.components.Component.Component`
* :class:`Sea.adapter.subsystems.Subsystem..Subsystem`
* :class:`Sea.adapter.connections.Connection.Connection`
* :class:`Sea.adapter.couplings.Coupling.Coupling`
* :class:`Sea.adapter.materials.Material.Material`
* :class:`Sea.adapter.excitations.Excitation.Excitation`

as well as the main class representing the model

* :class:`Sea.adapter.system.System.System`


The following figure gives an overview on how the classes are related.

.. graphviz::

    digraph overview {
      Subsystem -> Component -> System;
      Coupling -> Connection -> System;
      Connection -> Component
      Coupling -> Subsystem
      Coupling -> Component
      Component -> Material -> System
      Excitation -> Subsystem
    }
    
Additionaly, :mod:`FreeCAD` objects containing a Shape (like :mod:`Part` classes) are used for the geometry.
    
Components can have multiple subsystems. Depending on the type of component these are added automatically when creating a component.
If components are connected to eachother a connection needs to be created. The connection will automatically create all possible couplings between the subsystems.

Each :mod:`Sea.adapter` class inherits from a :mod:`Sea.model` class of the same type.

.. blockdiag::

    blockdiag adapter {
      Adapter -> Model;
    }


To perform an SEA analysis the document has to contain a geometry of the
structure under investigation. When the geometry is present, it is possible to
add SEA objects manually, or to construct a model automatically from the
geometry. Rudimentary rules are used to decide what types of each object should
be used. It is also possible to detect whether components connect and
automatically add the relevent type of connections and couplings. 

Next step is to set the properties of all the objects.
When all properties have been set, the modal energies can be solved. 
This can graphically be done by selecting an SEA System and then :menuselection:`Analysis --> Solve` or 
through Python by executing ``system.solve()`` where ``system`` is the :class:`FreeCAD.DocumentObject` of the ``system`` to be solved. 

=============
Model classes
=============
The :mod:`Sea.model` classes describe the physics involved in SEA. 
Several abstract base classes are available, describing properties common to each class of that type.
For instance, :class:`Sea.model.components.Component.Component` describes properties that are identical or mandatory for every component in :mod:`Sea.model.components`.

The model is written in Python and uses Numpy as well as Scipy. The classes described in the model can be used without FreeCAD. 
However, since all the linking would have to be done manually in such a case, this is not recommended.

The :ref:`reference` shows the implemented equations as well as sources.

===============
Adapter classes
===============
The :mod:`Sea.adapter` classes give FreeCAD access to the physics described in the :mod:`Sea.model` classes.
The adapter objects inherit from a :mod:`Sea.model` object of the respective class.

The adapter classes take care of setting values in the model and getting them out of the model. 
