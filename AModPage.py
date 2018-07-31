import sys

from PyQt5.QtCore import QCoreApplication, QDir, QFileInfo, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

if "mobase" not in sys.modules:
    import mock_mobase as mobase

class AModPage(mobase.IPluginModPage):
    
    def __init__(self):
        #QMessageBox.information(None, "__init__", "__init__")
        super(AModPage, self).__init__()

    def init(self, organizer):
        #QMessageBox.information(None, "init", "init")
        return True

    def name(self):
        #QMessageBox.information(None, "name", "name")
        return "Mod Page Support Plugin"

    def author(self):
        #QMessageBox.information(None, "author", "author")
        return "AnyOldName3"

    def description(self):
        #QMessageBox.information(None, "description", "description")
        return self.__tr("Adds support for a mod page.")

    def version(self):
        #QMessageBox.information(None, "version", "version")
        return mobase.VersionInfo(0, 1, 0, mobase.ReleaseType.prealpha)

    def isActive(self):
        QMessageBox.information(None, "isActive", "isActive")
        return True

    def settings(self):
        #QMessageBox.information(None, "settings", "settings")
        return []
    
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
        return QCoreApplication.translate("AModPage", str)
    
def createPlugin():
    return AModPage()