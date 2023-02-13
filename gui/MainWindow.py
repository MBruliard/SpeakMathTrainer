# -*- coding: utf-8 -*-
"""!
    @brief Customized MainWindow for SpeakMaths Trainer software
"""


##
# @file gui.MainWindow.py
#
# @brief Customized MainWindow for SpeakMaths Trainer software
#
# @date 2023-02-12
#
# @version 1.1
#
# @author MBruliard
##

import sys
import webbrowser
from os.path import isfile

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from gui.SessionWindow import SessionWindow

# Global Constants
# # Path to access the API documentation
API_PATH = 'api\html\index.html'

class MainWindow(QMainWindow):
    """!
        Class MainWindow 
        
        
        Defines the MainWindow of our application
        
    """    
    def __init__(self, parent):
        super().__init__()

        self.setWindowTitle("My App")
        self.setWindowTitle("SpeakMath Trainer")
        
        # Parent of the class
        self.parent = parent

        menu_bar = QMenuBar(self)        
        file_menu = QMenu("File", menu_bar)
        help_menu= QMenu("Help", menu_bar)
        new_action  = QAction('New', file_menu)
        new_action.triggered.connect(self.newSession)
        file_menu.addAction(new_action)
        
        exit_action = QAction("Exit", file_menu)
        exit_action.triggered.connect(self.quit)
        file_menu.addAction(exit_action)
        
        level_action = QAction('Explaination about Levels', help_menu)
        level_action.triggered.connect(self.inProgress)
        help_menu.addAction(level_action)
        
        about_action = QAction('About', help_menu)
        about_action.triggered.connect(self.inProgress)
        help_menu.addAction(about_action)
        
        api_action= QAction("API documentation", help_menu)
        api_action.triggered.connect(self.openAPI)
        help_menu.addAction(api_action)

        
        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(help_menu)
        self.setMenuBar(menu_bar)

        # Create central widget (QFrame)
        frame = self.createDefaultCentralWidget()
        self.setCentralWidget(frame)
        
        # size geometry
        self.setGeometry(100, 100, 300, 400)
        
        # open in full screen 
        #self.showMaximized()
    # ...
    
    
    def quit(self):
        """!
            @brief Event action to close the application        
        """
        self.close()
    # ...
    
    def inProgress(self):
        """
            @brief open a pop-up message window to inform the user that this section is 
            still in progress and so not available
        """
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Work in Progress")
        msg.setText("The application is still in development and some area are not available yet.\nPlease come back later with an update :)")
        
        # show
        msg.exec_()        
    # ...
    
     
    def createDefaultCentralWidget(self):
        """!
            @brief default central widget of the application - homepage
        """
        frame = QFrame();
        frame.setFrameShape(QFrame.StyledPanel)
        
        welcome = QLabel() 
        welcome.setAlignment(Qt.AlignCenter)
        welcome.setText('Welcome on SpeakMaths Trainer')

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(welcome)
        vbox.addStretch()

        frame.setLayout(vbox)
        return frame
    # ...
    
    def newSession(self):
        """!
            @brief Launch a new Session of operation by opening a SessionWindow on the central widget of the application     
        """
        self.setCentralWidget(SessionWindow(parent=self))
    # ...
    
    def openAPI(self):
        """!
            @brief Open the HTML API documentation with the default local navigator
        """
        
        webbrowser.open(API_PATH)
    # ...
    
# ...