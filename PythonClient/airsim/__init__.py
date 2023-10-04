import sys

# block imports during installation
if "setuptools" not in sys.modules:
    from .client import *
    from .utils import *
    from .types import *

__version__ = "1.8.1"
