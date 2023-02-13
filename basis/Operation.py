# -*- coding: utf-8 -*-
"""!
    @brief defines the Operation class for SpeakMaths Trainer software
"""

##
# @file basis.Operation.py
#
# @brief defines the Operation class for SpeakMaths Trainer software
#
# @date 2023-02-12
#
# @version 1.1
#
# @author MBruliard
##


from random import randint, uniform
from math import floor


# Global Constants
# # Authorized characters as operation
LIST_OPERATIONS =  ['+', '-', 'x', '/'];


class Operation:
    """!
        Definition of the class Operation
        
        @brief defines an elementary operation as addition, subtraction, product or division
    """
    
    
    def __init__(self, level=1, a=0, b=0, oper="+", minval=1, maxval=10):
        """!
            Class Constructor    
            
            @param level [int] difficulty level
            @param a [float] First number to operate
            @param b [float] Second number to operate
            @param oper [str] character representing the type of operation
            @param minval [float] minimal value to generate randomly @param a and @param b
            @param maxval [float] maximal value to generate randomly @param a and @param b
                        
        """
        if not isinstance(a, int) and not isinstance(a,float):
            raise TypeError("Error: parameter 'a' must be numeric.")
        # ...    
        if not isinstance(b, int) and not isinstance (b,float):
            raise TypeError("Error: parameters 'b' must be numeric.")
        # ...
        if (LIST_OPERATIONS + [None]).count(oper) == 0:
             raise TypeError("Error: parameter 'oper' must as value in LIST_OPERATIONS")
        # ...
        
        
        if oper is None:
            # Random choice in LIST_OPERATION
            oper = LIST_OPERATIONS[randint(0, len(LIST_OPERATIONS)-1)]
        # ...
        
        self.level = level;
        self.a = float(a);
        self.b = float(b);
        self.oper = oper;
        
        while (self.a == self.b) or (self.a == 0) or (self.b == 0) :
            if level == 1:
                self.generateLevelOneNumbers();
            elif level == 2:
                self.generateLevelTwoNumbers(minval, maxval)
            elif level == 3:
                self.generateLevelThreeNumbers(minval, maxval)
            else:
                self.generateLevelFourNumbers(minval, maxval)
            # ...
        # ...
    
        self.res = self.computeResult();

    # ...
    
    
    def __str__(self):
        """!
            @brief Redefines the standard console output of the class
        """
        return "{0} {1} {2} = {3}".format(self.a, self.oper, self.b, self.res)
    # ...
    
    def computeResult(self):
        """!
            @brief Compute the solution of the operation        
        """
        if self.oper == "+":
            return self.a + self.b
        elif self.oper == "-":
            return self.a - self.b
        elif self.oper == "x":
            return self.a * self.b
        else:
            return self.a / self.b
        # ...
    # ...
    
     
    def generateLevelOneNumbers(self):
        """
            @brief generate @param a @param b based on the rules of the 1st level of difficulty
            
            @details Level 1 : values between 1 and 10. Pas de retenue: a > b
        """
        
        a = randint(1, 10);
        b = randint(a, 10);
        
        self.b = a;
        self.a = b;
    # ...
    
    
    def generateLevelTwoNumbers(self, minval, maxval):
        """!
            @brief generate @param a @param b based on the rules of the 2nd level of difficulty
            
            @details Level 2 : values chosen betwen min and max values. a > b. Pas de retenue
            
            @param minval [float] minimal value to generate randomly @param a and @param b
            @param maxval [float] maximal value to generate randomly @param a and @param b
        """    
        
        self.a = randint(minval, maxval);
        
        dec = decomposition(self.a);
        b = [];
        for i in range(0, len(dec)):
            b.append(randint(0, dec[i]));
        # ...
        self.b = int(''.join([str(i) for i in b]))    
    # ...
    
    def generateLevelThreeNumbers(self, minval, maxval):
        """
            @brief generate @param a @param b based on the rules of the 3rd level of difficulty
            
            @details Level 3 : euclidian division with 1 number. Else everything is possible
            
            @param minval [float] minimal value to generate randomly @param a and @param b
            @param maxval [float] maximal value to generate randomly @param a and @param b
        """    
        
        self.a = uniform(minval, maxval)
        self.b = uniform(minval, maxval)
        
        if self.oper == "/":
            self.b = randint(1, 9);
            self.a = randint(1, 100)*self.b;
        # ...
    # ...
    
    def generateLevelFourNumbers(self, minval, maxval):
        """
            @brief generate @param a @param b
            
            @param minval [float] minimal value to generate randomly @param a and @param b
            @param maxval [float] maximal value to generate randomly @param a and @param b
        """    
        
        self.a = uniform(minval, maxval)
        self.b = uniform(minval, maxval)
        if self.oper == "/":
            self.b = randint(2, floor(min(self.a, self.b)));
        # ...  
    # ...
    
# ... end class


# Functions
def decomposition(n):
    """!
        Generates the base 10 decomposition of a number
        
        @param n [int] integer number
        @return base 10 decomposition of @parma n in a list 
    """
    result = []
    while n > 0:
        result.append(n % 10)
        n = n // 10
    # ...
    return result[::-1];
# ...