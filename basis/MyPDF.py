# -*- coding: utf-8 -*-
"""!
    @brief Customized PDF writer package for SpeakMaths Trainer software
"""

##
# @file basis.MyPDF.py
#
# @brief Customized PDF writer package for SpeakMaths Trainer software
#
# @date 2023-02-12
#
# @version 1.1
#
# @author MBruliard
##


from math import floor
from basis.Operation import decomposition

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class MyPDF (canvas.Canvas): 
    """!
        The PDF Writing class
        
        Definition of the class MyPDF that create a PDF file from a list of operations stored in @class Session
    """    
    
    def __init__ (self, filename):
        """!
            @brief Class constructor
            
            @param filename local path to save the PDF file obtain 
        """
        super().__init__(filename, pagesize=A4)
        
        
        self.width, self.height = A4
        self.marginTop = 80;
        self.marginBottom = 100;
        self.marginLeft = 50
        self.marginRight = 50;
        
        self.writeHeader()
          
    # ...
    
    
    def newPage(self):
        """!
            @brief add a new page to the PDF file
            
            
        """
        self.showPage()
        self.writeHeader()
        
    # ...
    
    
    def writeText(self, text, w, h, fontsize=12):
        """!
            @brief write some text on the PDF file.
            
            @param text [str]   text to write
            @param w    [float] horizontal position of the text. Start from the left
            @param h    [float] vertical position of the text. Start from the top
            @param fontsize [int] define the fontsize of the text. Set at 12pt per default
        """
        self.setFont("Helvetica", fontsize)
        self.drawString(self.marginLeft + w, self.height - self.marginTop - h, text)
    # ...
    
    
    def writeParagraph(self, text, w, h, fontsize=12):
        """!
            @brief Write a paragraph. Mainly use in case of a long text that could possibly be longer than the linewidth of the page
        
            @param text [str]   text to write
            @param w    [float] horizontal position of the text. Start from the left
            @param h    [float] vertical position of the text. Start from the top
            @param fontsize [int] define the fontsize of the text. Set at 12pt per default
        """
        content = self.beginText(w, self.height - self.marginTop - h);
        content.setFont("Helvetica", fontsize)
        content.textLines(text)
        self.drawText(content)
    # ...
    
    
    def writeHeader(self):
        """!
            @brief defines the Header style of a page. Used on each page of the PDF file
        """
        self.writeParagraph("Printed with SpeakMath Trainer", self.marginLeft, 
                            -25, fontsize=10)
        self.writeText("Page %s" % self.getPageNumber(), 
                       self.width - 3*self.marginRight, 
                       -25, fontsize=10)
        
        self.line(self.marginLeft, self.height - self.marginTop, 
                  self.width - self.marginRight,  self.height - self.marginTop)
    # ...
    
    
    def writeOperation(self, operation, w, h, fontsize=12):
        """!
            @brief Display a well-posed elementary operation
            
            @param operation [basis.Operation]  Operation to display
            @param w    [float] horizontal position of the text. Start from the left
            @param h    [float] vertical position of the text. Start from the top
            @param fontsize [int] define the fontsize of the text. Set at 12pt per default
        """
        
        self.setFont("Helvetica", fontsize)
        
        # find max length 
        deca = decomposition(operation.a)
        decb = decomposition(operation.b)
        mla = len(deca)
        mlb = len(decb)
        
        ml = max(mla, mlb)
        
        # spacing
        sp = 20
        
        if operation.oper == '/':
            
            # line 1
            for j in range(0, mla):
                self.writeText(str(deca[j]), w + (j+1)*sp, h)
            # ...
            for j in range(0, mlb):
                self.writeText(str(deca[j]), w + + sp +(mla+j+1)*sp, h)
            # ...
            
            # then we draw the vertical line
            self.line(w + self.marginLeft + (mla + 1.5)*sp, 
                      self.height - self.marginTop - (h - sp), 
                      w + self.marginLeft + (mla + 1.5)*sp, 
                      self.height - self.marginTop - (h + 4*sp))
            
            # then we draw the horizontal line
            self.line(w + self.marginLeft + sp, 
                      self.height - self.marginTop - (h + 0.5*sp), 
                      w + self.marginLeft + (ml+2.5)*sp, 
                      self.height - self.marginTop - (h + 0.5*sp))
            
        else:
            # first we draw the value of a
            for j in range(0, mla):
                self.writeText(str(deca[j]), w + (ml - mla + 1)*sp + (j+1)*sp, h)
            # ...
            
            # second line
            self.writeText(operation.oper, w + sp, h + sp)
            for j in range(0, mlb):
                self.writeText(str(decb[j]), w + (ml - mlb + 1)*sp + (j+1)*sp, h+sp)
            # ...
            
            # trace
            self.line(w + self.marginLeft + sp, 
                      self.height - self.marginTop - (h + 2*sp), 
                      w + self.marginLeft + (ml+2)*sp, 
                      self.height - self.marginTop - (h + 2*sp))
                    
            # results
            for i in range(0, ml+1):
                self.writeText(".", w+(ml+1)*sp, h + 3*sp)
            # ...
        # ...
        
    # ...
# ....