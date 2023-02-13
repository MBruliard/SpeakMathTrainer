# -*- coding: utf-8 -*-
"""!
    @brief Main Program for SpeakMaths Trainer
    @date 2023-02-13
    @version 1.1
"""

import sys
from PyQt5.QtWidgets import QApplication

from gui.MainWindow import MainWindow
from gui.SessionWindow import SessionWindow

from basis.Session import Session


def main():
    """!
        Main Program
    """
    # check optional arguments
    args = sys.argv[0:]
    if len(args) > 1 and args[1] == '-nogui':
        lev = int(input("Level of Operations ? "))
        n = int(input('Number of operations desired ? '));
        
        session = Session(n, lev);
        print(session)
        session.export("test.pdf")
    else:
    
        app = QApplication(sys.argv)
        
        window = MainWindow(parent=app)
        window.show()
        
        sys.exit(app.exec_())
    # ...
# ...
    

if __name__ == "__main__":
    main()
# ...