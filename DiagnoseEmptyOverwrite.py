import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog

if "mobase" not in sys.modules:
    import mock_mobase as mobase

class DiagnoseEmptyOverwrite(mobase.IPluginDiagnose, mobase.IPluginModPage):
    
    def __init__(self):
        super(DiagnoseEmptyOverwrite, self).__init__()
        mobase.IPluginModPage.__init__(self)
        self.__organizer = None

    def init(self, organizer):
        self.__organizer = organizer
        
        # Python doesn't like multi-line anonymous functions
        organizer.modList().onModStateChanged(lambda modName, modState : self._invalidate() if modName == "Overwrite" or modName == u"Overwrite" else None)
        
        return True

    def name(self):
        return "Empty Overwrite Diagnosis... with a mod page!"

    def author(self):
        return "AnyOldName3"

    def description(self):
        return self.__tr("Complains and bitches if your overwrite directory is empty... and adds a nearly useless mod page!")

    def version(self):
        return mobase.VersionInfo(2, 0, 0, mobase.ReleaseType.final)

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
    
    def displayName(self):
        #QMessageBox.information(None, "displayName", "displayName")
        return "Probably TES Alliance"
    
    def icon(self):
        #QMessageBox.information(None, "icon", "icon")
        return QIcon()
    
    def pageURL(self):
        #QMessageBox.information(None, "pageURL", "pageURL")
        return QUrl("http://tesalliance.org")
    
    def useIntegratedBrowser(self):
        #QMessageBox.information(None, "useIntegratedBrowser", "useIntegratedBrowser")
        return True
    
    def handlesDownload(self, pageURL, downloadURL, fileInfo):
        QMessageBox.information(None, "handlesDownload", "handlesDownload")
        
        import re
        if not re.match(r"https?://tesalliance.org/forums/index.php\?/files/download/([0-9]+)-([^/]+)/", pageURL.toString()):
            return False
        if not re.match(r"https?://tesalliance.org/forums/index.php\?/files/getdownload/([0-9]+)-([^/]+)/", downloadURL.toString()):
            return False
        
        # We now need to set the fields of fileInfo
        
        return True
    
    def setParentWidget(self, widget):
        #QMessageBox.information(None, "setParentWidget", "setParentWidget")
        pass
    
    def __tr(self, str):
        return QCoreApplication.translate("DiagnoseEmptyOverwrite", str)
    
def createPlugin():
    return DiagnoseEmptyOverwrite()