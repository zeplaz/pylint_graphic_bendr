# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 01:56:54 2023

@author: ioz
"""



# -*- coding: utf-8 -*-
"""

"""


 
    
    #you COULD just import core, but this would make the namespace dispear lamme. keep it 
    # does not make much sense this small butt. for biger names like it does 
import core as core 
"""this wont work unless yuo move that top part to its own file core.py
"""


import sys

def main():
    
    if len(sys.argv) < 1:   
        #here you call it like this as its a static method so you call with the class name 
        print(core.Process.Help())

   else:
       core_process_instance = core.Process(sys.argv)
       while(run):
           run = core_process_instance.cyclework()
       
    print("Compleated:normalshutdown clean begins.")
    
    


if __name__ == "__main__":
    sys.exit(main())
    print("Shutdown-final")
    
    return 0
