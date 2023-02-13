# -*- coding: utf-8 -*-
"""!
    @brief Defines the class Session for SpeakMaths Trainer software
"""

##
# @file basis.Session.py
#
# @brief Defines the class Session for SpeakMaths Trainer software
#
# @date 2023-02-12
#
# @version 1.1
#
# @author MBruliard
##

from basis.Operation import *
from basis.MyPDF import *

import time

# Functions 
def countdown_timer(seconds):
    """!
       @brief Creates a countdown timer and display it on the standard console
       
       @param seconds length of the countdown
    """
    for i in range(seconds, 0, -1):
        print(i, end='\r')
        time.sleep(1)
    print("Time's up!")
# ...


class Session:
    """!
        The Session class 
        
        @brief defines a list of operations to compute
    """    
  
    def __init__(self, n, level, oper=None, minval=1, maxval=10):
        """!
            Class Constructor
            
            @param n [int] number of operations
            @param level [int] level of difficulty of the list of operations
            @param oper [str] symbol of the type of operation. See basis.Operation.LIST_OPERATIONS
            @param minval [float] minimum possible value to use to generate numbers in Operation
            @param maxval [float] maximum possible value to use to generate numbers
            
        """
        if not isinstance(n, int) or n < 1:
            raise TypeError('Error: Argument n must be a strict positive integer')
        # ...
        
        if not isinstance(level, int) or not 1 <= level <= 4:
            raise TypeError('Error: Argument level must be a strict positive integer between 1 and 4 included')
        # ...
        
        # Number of operations
        self.n = n; 
        
        # Difficulty level
        self.level = level;
        
        # List of operations to store
        self.list = [];
        
        if oper == None:
            oper = LIST_OPERATIONS;
        # ...
        if type(oper) is str:
            oper = [oper]
        # ...
        
        for i in range(0, n):
            opr = LIST_OPERATIONS[randint(0, len(oper)-1)]
            self.list.append(Operation(level=level, a=0, b=0, oper=opr, minval=minval, maxval=maxval))
        # ...
    # ...
    
    def __str__(self):
        """!
            @brief Redefines the standard console output of the class 
        """
        return "\n".join([str(i) for i in self.list])
    # ...
    
    
    def export(self, filename):
        """!
            @brief Export the session into a PDF file.
            
            @param filename Path of the file to save it on the local computer
        """
        f = MyPDF(filename)
        
        start_l = f.marginTop + 20
        start_c = f.marginLeft 
        
        step_c  = (f.width - f.marginLeft - f.marginRight)/2
        step_l = 150
        
        textheight = f.height - 2*f.marginTop
        nb_per_page = textheight // step_l
        
        pos_l = start_l
        pos_c = [start_c, step_c + start_c]
        for i in range(0, self.n):
            
            print("{0}\t|{1} {2}".format(i, pos_c[i%2], pos_l))
            f.writeOperation(self.list[i], pos_c[i%2],  pos_l)
        
            # change position for next it
            pos_l = pos_l + (i % 2)*step_l            
            if i!= 0 and i % nb_per_page == 0:
                f.newPage()
                pos_l = start_l
            # ...
            
        # ...
        
        f.save()   
    # ...
# ...