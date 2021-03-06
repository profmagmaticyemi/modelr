from bruges import reflection
import bruges.filters as wavelet

"""
This file holds data strctures and constants used in the modelr
application
"""

REFLECTION_MODELS = {
    'zoeppritz': reflection.zoeppritz,
    'zoeppritz_rpp': reflection.zoeppritz_rpp,
    'akirichards': reflection.akirichards,
    'akirichards_alt': reflection.akirichards_alt,
    'fatti': reflection.fatti,
    'shuey2': reflection.shuey2,
    'shuey3': reflection.shuey3,
    'bortfeld2': reflection.bortfeld2,
    'bortfeld3': reflection.bortfeld3,
}

WAVELETS = {
    'ricker': wavelet.ricker,
    'ormsby': wavelet.ormsby,
    #    'sweep': wavelet.sweep
}

dt = 0.001
wavelet_duration = 0.2
