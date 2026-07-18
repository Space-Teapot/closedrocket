"""Rocket class and related utilities for closedrocket."""

import numpy as np

# Module docstring
__all__ = ["Rocket"]


class Rocket:
    """Rocket class representing a rocket's physical properties and state.
    
    Attributes:
        mass (float): Mass of the rocket [kg]
        lref (float): Reference length of the rocket [m]
        sref (float): Reference area of the rocket [m^2]
        Cd (np.ndarray): Drag coefficient as a function of Mach number
        Cm (np.ndarray): Moment coefficient as a function of Mach number and angle of attack
        MOI (np.ndarray): Moment of inertia tensor of the rocket [kg*m^2]
    """
    
    def __init__(self, mass: float, lref: float, sref: float, Cd: np.ndarray, Cm: np.ndarray, MOI: np.ndarray):
        """Initialize a Rocket instance with given physical properties."""
        self.mass = mass
        self.lref = lref
        self.sref = sref
        self.Cd = Cd
        self.Cm = Cm
        self.MOI = MOI  # PLACEHOLDER: use the provided moment of inertia tensor