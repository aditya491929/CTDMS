import os
import sys
def initialize():
    backendModulePath = os.path.dirname(os.path.dirname(__file__))+"/backend"
    sys.path.append(backendModulePath)