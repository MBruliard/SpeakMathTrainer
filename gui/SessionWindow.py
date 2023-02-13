# -*- coding: utf-8 -*-
"""!
    @brief Customized SessionWindow for SpeakMaths Trainer GUI interface
"""


##
# @file gui.SessionWindow.py
#
# @brief Customized SessionWindow for SpeakMaths Trainer GUI interface
#
# @date 2023-02-12
#
# @version 1.1
#
# @author MBruliard
##



from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from basis.Session import Session

import sys
import subprocess


class SessionWindow(QFrame):
    """!
        Defines the SessionWindow class
        
        Creates a Frame for the GUI interface of the software. Allow the user to define parameters for a new session
    """
    
    def __init__(self, parent=None):
        """!
            @brief Class Constructor
        """
        super().__init__()
        
        # Parent of the Frame
        self.parent = parent
    
        self.setFrameShape(QFrame.StyledPanel)
        
        # Main Layout
        self.layout = QVBoxLayout(self)
              
        # Frame title
        self.title_frame = QLabel('New Session')
        self.title_frame.setAlignment(Qt.AlignCenter)
        
        self.layout.addStretch()
        self.layout.addWidget(self.title_frame)
        self.layout.addStretch()
        
        # nbr of operation
        nb_wid = QWidget(self)
        nb_layout = QHBoxLayout()
        nb_layout.setAlignment(Qt.AlignLeft)
        nb_wid.setLayout(nb_layout)
        
        nb_layout.addWidget(QLabel('Number of Operations:'))
        self.nb_operations = QSpinBox(self)
        self.nb_operations.setSingleStep(1)
        self.nb_operations.setMinimum(1)       
        nb_layout.addWidget(self.nb_operations)
        
        self.layout.addWidget(nb_wid)
        
        # level choice
        level_wid = QWidget(self)
        
        level_layout= QHBoxLayout()
        level_layout.setAlignment(Qt.AlignLeft)
        level_wid.setLayout(level_layout)
        
        level_layout.addWidget(QLabel('Level:'))
        
        self.group_level = QButtonGroup(self)
        
        self.button_lev1 = QRadioButton('1', self)
        self.group_level.addButton(self.button_lev1)
        
        self.button_lev2 = QRadioButton('2', self)
        self.group_level.addButton(self.button_lev2)
        
        self.button_lev3 = QRadioButton('3', self)
        self.group_level.addButton(self.button_lev3)
        
        self.button_lev4 = QRadioButton('4', self)
        self.group_level.addButton(self.button_lev4)
        
        level_layout.addWidget(self.button_lev1)
        level_layout.addWidget(self.button_lev2)
        level_layout.addWidget(self.button_lev3)
        level_layout.addWidget(self.button_lev4)
        
        
        self.layout.addWidget(level_wid)
        
        #  operation type 
        oper_wid = QWidget(self)
        oper_layout = QHBoxLayout()
        oper_layout.setAlignment(Qt.AlignLeft)
        oper_wid.setLayout(oper_layout)
        
        self.button_op1 = QCheckBox('Addition', self)
        self.button_op2 = QCheckBox('Subtraction', self)
        self.button_op3 = QCheckBox('Product', self)
        self.button_op4 = QCheckBox('Division', self)
       
        oper_layout.addWidget(self.button_op1)
        oper_layout.addWidget(self.button_op2)
        oper_layout.addWidget(self.button_op3)
        oper_layout.addWidget(self.button_op4)
        
        
        self.layout.addWidget(oper_wid)
        
        # min and max possible values 
        range_wid = QWidget(self)
        range_layout = QHBoxLayout()
        range_layout.setAlignment(Qt.AlignLeft)
        range_wid.setLayout(range_layout)
        
        range_layout.addWidget(QLabel('Minimum Value:'))
        self.minval = QSpinBox(self)
        self.minval.setSingleStep(1)   
        range_layout.addWidget(self.minval)
        
        range_layout.addWidget(QLabel('Maximum Value:'))
        self.maxval = QSpinBox(self)
        self.maxval.setSingleStep(1)   
        range_layout.addWidget(self.maxval)
               
        
        self.layout.addWidget(range_wid)
    
        # define buttons
        self.layout.addStretch()
        
        button_wid = QWidget(self)
        
        button_group = QHBoxLayout()
        button_group.setAlignment(Qt.AlignRight)
        button_wid.setLayout(button_group)
        
        ok_button = QPushButton('OK')
        ok_button.clicked.connect(self.run)
        
        clear_button = QPushButton('Clear')
        clear_button.clicked.connect(self.setDefaultEntryValues)

        button_group.addWidget(clear_button)                             
        button_group.addWidget(ok_button)
        
        self.layout.addWidget(button_wid)
        
        # define default parameters
        self.setDefaultEntryValues()
        
    # ...
    
    
    def setDefaultEntryValues(self):
      """!
          @brief defines the default values of the parameters of the interface
      """
      self.button_lev3.setChecked(True)
      self.button_op1.setChecked(True)
      self.button_op2.setChecked(True)
      self.button_op3.setChecked(True)
      
      self.minval.setValue(1)
      self.maxval.setValue(100)
      
      self.nb_operations.setValue(10)
    # ...
    
    
    def run(self):
        """! 
            @brief Event action for the OK button        
        """
        # get infos from GUI
        nb = self.nb_operations.value()
        level = int(self.group_level.checkedButton().text())
        
        available_oper = [];
        if self.button_op1.isChecked():
            available_oper.append('+')
        # ...
        if self.button_op2.isChecked():
            available_oper.append('-')
        # ...
        if self.button_op3.isChecked():
            available_oper.append('x')
        # ...
        if self.button_op4.isChecked():
            available_oper.append('/')
        # ...
        print(available_oper)
        
        minval = self.minval.value()
        maxval = self.maxval.value()
        
        # create Session
        session = Session(n=nb, level=level, oper=available_oper, minval=minval, maxval=maxval)
        
        # export as PDF file
        # --  open a File Opener to define where to save it
        fname = QFileDialog.getSaveFileName(self, 'Save file', 
         'C:\\Documents',"*.pdf")
        
        if fname[0] != '':
            fname = fname[0]
            session.export(fname)
            
            # --  opening the file in standard PDF viewer
            if sys.platform == 'win32':
                subprocess.Popen(f'AcroRd32.exe {fname}', shell=True)
            else:
                subprocess.Popen(['xdg-open', fname], shell=True)
        # ...
    # ...
    
# ...
