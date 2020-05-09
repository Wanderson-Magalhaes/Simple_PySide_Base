################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 0.1
##
################################################################################

# GUI FILE
from main import *
class Functions(MainWindow):

    ## ==> GLOBALS
    globals()['state'] = 0
    globals()['titleBar'] = True

    ########################################################################
    ## START - GUI FUNCTIONS
    ########################################################################

    ## ==> MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self):
        status = globals()['state']
        if status == 0:
            self.showMaximized()
            globals()['state'] = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(30, 30, 30)")
            self.ui.frame_size_grip.hide()
        else:
            self.showNormal()
            globals()['state'] = 0
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(30, 30, 30, 150)")
            self.ui.frame_size_grip.show()

    ## ==> RETURN STATUS
    def returStatus():
        return globals()['state']

    ## ==> SET STATUS
    def setStatus(status):
        globals()['state'] = status

    ## ==> TOGGLE MENU
    ########################################################################
    def toggleMenu(self, maxWidth):
        width = self.ui.frame_left_menu.width()
        maxExtend = maxWidth
        standard = 70

        # SET MAX WIDTH
        if width == 70:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTitleBar(status):
        globals()['titleBar'] = status

    ########################################################################
    ## END - GUI FUNCTIONS
    ########################################################################


    ########################################################################
    ## START - GUI DEFINITIONS
    ########################################################################

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):
        ## REMOVE ==> STANDARD TITLE BAR
        if globals()['titleBar']:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_top_btns.hide()
            self.ui.frame_size_grip.hide()
            self.ui.frame_top.setMinimumHeight(50)
            self.ui.frame_top.setMaximumHeight(50)

        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        ### ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(lambda: Functions.maximize_restore(self))

        ## SHOW ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(lambda: self.close())

    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################
