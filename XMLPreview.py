import sys

from PyQt5.QtCore import QCoreApplication, QDir, QFileInfo, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QTextEdit

if "mobase" not in sys.modules:
    import mock_mobase as mobase

class AClass(object):
    pass

class XMLPreview(mobase.IPluginPreview):
    
    def __init__(self):
        #QMessageBox.information(None, "__init__", "__init__")
        #QMessageBox.information(None, "Types", "str(type(mobase.IPluginPreview)) = " + str(type(mobase.IPluginPreview)) + ", " + mobase.IPluginPreview.__name__)
        #dirStuff = dir(mobase.IPluginPreview)
        #dirString = ""
        #for item in dirStuff:
        #    dirString += item
        #    dirString += ": "
        #    dirString += str(type(getattr(mobase.IPluginPreview, item)))
        #    dirString += " = '"
        #    dirString += str(getattr(mobase.IPluginPreview, item))
        #    dirString += "'\n"
        #QMessageBox.information(None, "Dir", dirString)
        #QMessageBox.information(None, "Types", "str(type(XMLPreview)) = " + str(type(XMLPreview)))
        #QMessageBox.information(None, "Types", "str(type(QMessageBox)) = " + str(type(QMessageBox)))
        #QMessageBox.information(None, "Types", "str(type(AClass)) = " + str(type(AClass)))
        
        super(XMLPreview, self).__init__()

    def init(self, organizer):
        #QMessageBox.information(None, "init", "init")
        return True

    def name(self):
        #QMessageBox.information(None, "name", "name")
        return "XML Preview Plugin"

    def author(self):
        #QMessageBox.information(None, "author", "author")
        return "AnyOldName3"

    def description(self):
        #QMessageBox.information(None, "description", "description")
        return self.__tr("Lets you preview XML files (but without any fancy syntax highlighting, unfortunately).")

    def version(self):
        #QMessageBox.information(None, "version", "version")
        return mobase.VersionInfo(0, 1, 0, mobase.ReleaseType.prealpha)

    def isActive(self):
        #QMessageBox.information(None, "isActive", "isActive")
        return True

    def settings(self):
        #QMessageBox.information(None, "settings", "settings")
        return []
    
    def supportedExtensions(self):
        #QMessageBox.information(None, "isActive", "isActive")
        return ["xml"]
    
    def genFilePreview(self, fileName, maxSize):
        #QMessageBox.information(None, "isActive", "isActive")
        textEdit = QTextEdit()
        with open(fileName, 'r') as fileHandle:
            textEdit.setText(fileHandle.read())
        textEdit.setReadOnly(True)
        return textEdit
    
    def __tr(self, str):
        return QCoreApplication.translate("XMLPreview", str)
    
def createPlugin():
    return XMLPreview()