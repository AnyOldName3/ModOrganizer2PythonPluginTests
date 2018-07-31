import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog

if "mobase" not in sys.modules:
    import mock_mobase as mobase

class DiagnoseEmptyOverwrite(mobase.IPluginDiagnose):
    
    def __init__(self):
        super(DiagnoseEmptyOverwrite, self).__init__()
        self.__organizer = None

    def init(self, organizer):
        self.__organizer = organizer
        
        # Python doesn't like multi-line anonymous functions
        organizer.modList().onModStateChanged(lambda modName, modState : self._invalidate() if modName == "Overwrite" or modName == u"Overwrite" else None)
        
        return True

    def name(self):
        return "Empty Overwrite Diagnosis"

    def author(self):
        return "AnyOldName3"

    def description(self):
        return self.__tr("Complains and bitches if your overwrite directory is empty.")

    def version(self):
        return mobase.VersionInfo(1, 1, 0, mobase.ReleaseType.final)

    def isActive(self):
        return True

    def settings(self):
        return []
    
    def activeProblems(self):
        overwrite = self.__organizer.overwritePath()
        if os.listdir(overwrite) == []:
            return [0]
        else:
            return []
    
    def shortDescription(self, key):
        return self.__tr("Empty Overwrite directory")
    
    def fullDescription(self, key):
        return self.__tr("You've got nothing in your Overwrite directory. No human has any need to be <i>that</i> tidy. Press 'Fix' to create a blank file in the Overwrite directory.")
    
    def hasGuidedFix(self, key):
        return True
    
    def startGuidedFix(self, key):
        open(os.path.join(self.__organizer.overwritePath(), "blank file.txt"), 'a').close()
        self.__organizer.refreshModList()
        QMessageBox.information(None, self.__tr("File Created"), self.__tr("A blank file has been created in your Overwrite directory"))
    
    def __tr(self, str):
        return QCoreApplication.translate("DiagnoseEmptyOverwrite", str)
    
def createPlugin():
    return DiagnoseEmptyOverwrite()
