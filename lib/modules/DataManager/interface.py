# -*- coding: utf-8 -*-
from DataManagerTemplate import *
from lib.modules.Module import *
from lib.DataManager import *
import os, re, sys, time

class DataManager(Module):
    def __init__(self, manager, name, config):
        Module.__init__(self, manager, name, config)
        self.dm = self.manager.dataManager
        self.win = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.dialog = QtGui.QFileDialog()
        self.dialog.setFileMode(QtGui.QFileDialog.DirectoryOnly)
        ## Load values into GUI
        self.model = DMModel(self.manager.getBaseDir())
        self.ui.fileTreeView.setModel(self.model)
        self.baseDirChanged()
        self.currentDirChanged()
        
        
        ## Make all connections needed
        #QtCore.QObject.connect(self.dm, QtCore.SIGNAL("baseDirChanged()"), self.baseDirChanged)
        QtCore.QObject.connect(self.ui.selectDirBtn, QtCore.SIGNAL("clicked()"), self.showFileDialog)
        QtCore.QObject.connect(self.ui.setCurrentDirBtn, QtCore.SIGNAL("clicked()"), self.setCurrentClicked)
        #QtCore.QObject.connect(self.ui.storageDirText, QtCore.SIGNAL('textEdited(const QString)'), self.selectDir)
        QtCore.QObject.connect(self.dialog, QtCore.SIGNAL('filesSelected(const QStringList)'), self.setBaseDir)
        QtCore.QObject.connect(self.manager, QtCore.SIGNAL('baseDirChanged'), self.baseDirChanged)
        QtCore.QObject.connect(self.manager, QtCore.SIGNAL('currentDirChanged'), self.currentDirChanged)
        QtCore.QObject.connect(self.ui.newFolderList, QtCore.SIGNAL('currentIndexChanged(int)'), self.newFolder)
        QtCore.QObject.connect(self.ui.fileTreeView.selectionModel(), QtCore.SIGNAL('selectionChanged(const QItemSelection&, const QItemSelection&)'), self.fileSelectionChanged)
        self.win.show()
        
    def updateNewFolderList(self):
        conf = self.manager.conf['folderTypes']
        self.ui.newFolderList.clear()
        self.ui.newFolderList.addItems(['New...', 'Folder'] + conf.keys())
        
    def baseDirChanged(self):
        dh = self.manager.getBaseDir()
        self.baseDir = dh
        self.ui.baseDirText.setText(QtCore.QString(dh.dirName()))
        self.model.setBaseDirHandle(dh)
        self.currentDirChanged()

    def setCurrentClicked(self):
        newDir = self.selectedFile()
        if not os.path.isdir(newDir):
            newDir = os.path.split(newDir)[0]
        dh = self.manager.dirHandle(newDir)
        self.manager.setCurrentDir(dh)

    def currentDirChanged(self):
        newDir = self.manager.getCurrentDir()
        dirName = newDir.dirName(relativeTo=self.baseDir)
        self.ui.currentDirText.setText(QtCore.QString(dirName))
        self.model.setCurrentDir(newDir.dirName())
        dirIndex = self.model.findIndex(newDir.dirName())
        self.ui.fileTreeView.setExpanded(dirIndex, True)
        self.ui.fileTreeView.scrollTo(dirIndex)
        
        # refresh file tree view
        
    def showFileDialog(self):
        self.dialog.setDirectory(self.manager.getBaseDir().dirName())
        self.dialog.show()

    def setBaseDir(self, dirName):
        #if dirName is None:
            #dirName = QtGui.QFileDialog.getExistingDirectory()
        if type(dirName) is QtCore.QStringList:
            dirName = str(dirName[0])
        elif type(dirName) is QtCore.QString:
            dirName = str(dirName)
        if dirName is None:
            return
        if os.path.isdir(dirName):
            self.manager.setBaseDir(dirName)
        else:
            raise Exception("Storage directory is invalid")
            
    def selectedFile(self):
        sel = list(self.ui.fileTreeView.selectedIndexes())
        if len(sel) == 1:
            index = sel[0]
        else:
            raise Exception("Error - multiple/no items selected")
        return self.model.getFileName(index)

    def newFolder(self):
        if self.ui.newFolderList.currentIndex() == 0:
            return
            
        ftype = str(self.ui.newFolderList.currentText())
        self.ui.newFolderList.setCurrentIndex(0)
        
        cdir = self.manager.getCurrentDir()
        if ftype == 'Folder':
            nd = cdir.mkdir('NewFolder', autoIncrement=True)
            item = self.model.dirIndex(nd)
            self.ui.fileTreeView.edit(item)
        else:
            spec = self.manager.conf['folderTypes'][ftype]
            name = spec['name']
            if "%d" in name:
                name = name.replace('%d', time.strftime('%Y.%m.%d'))
                
            ## Determine where to put the new directory
            parent = cdir
            try:
                checkDir = cdir
                for i in range(5):
                    if not checkDir.isManaged():
                        break
                    inf = checkDir.info()
                    if 'dirType' in inf and inf['dirType'] == spec:
                        parent = checkDir.parent()
                        break
                    checkDir = checkDir.parent()
            except:
                sys.excepthook(*sys.exc_info())
                print "Error while deciding where to put new folder (using currentDir by default)"
            
            ## make
            nd = parent.mkdir(name, autoIncrement=True)
            
            ## Add meta-info
            info = {'dirType': spec}
            nd.setInfo(info)
            
            ## set display to info
            self.showFileInfo(nd)
            
            
        self.manager.setCurrentDir(nd)


    def fileSelectionChanged(self):
        self.ui.fileInfo.setCurrentFile(self.selectedFile())
        #if type(f) is str:
            
            #pass
        #elif isinstance(f, DirHandle):
            #if f.isManaged():
                #info = f.info()
                #if 'dirType' in info:
                    ### generate form for this dirType
                    #pass
                #else:
                    ### generate default form
                    #pass
                    
            #else:
                ### Unmanaged, display directory name and clear all widgets
                #pass
                
        
        
        
        
        
        

class DMModel(QtCore.QAbstractItemModel):
    """Based on DirTreeModel, used for displaying the contents of directories created and managed by DataManager"""
    def __init__(self, baseDirHandle=None, parent=None):
        QtCore.QAbstractItemModel.__init__(self, parent)
        self.baseDir = baseDirHandle
        self.currentDir = None
        self.paths = {}
        self.dirCache = {}
        self.handles = {}
        
    def setBaseDirHandle(self, d):
        if self.baseDir is not None:
            self.unwatch(self.baseDir)
        self.baseDir = d
        self.watch(self.baseDir)
        self.clearCache()
        
    def setCurrentDir(self, d):
        self.currentDir = d
        
    def watch(self, d):
        if not isinstance(d, QtCore.QObject):
            raise Exception("Can not watch object of type %s" % str(type(d)))
        #print "watch", d, d.dirName()
        QtCore.QObject.connect(d, QtCore.SIGNAL('changed'), self.dirChanged)
        
    def unwatch(self, d):
        if not isinstance(d, QtCore.QObject):
            raise Exception("Can not unwatch object of type %s" % str(type(d)))
        QtCore.QObject.disconnect(d, QtCore.SIGNAL('changed'), self.dirChanged)
        
    def clearCache(self, path=None):
        if path is None:
            for k in self.handles:
                self.unwatch(self.handles[k])
            self.dirCache = {}
            self.paths = {}
            self.handles = {}
            self.emit(QtCore.SIGNAL('layoutChanged()'))
            #self.reset()
            return
        if path in self.dirCache:
            #del self.dirCache[path]
            rm = []
            for k in self.paths:
                if path == k[:len(path)]:
                   rm.append(k)
            for k in rm:
                del self.paths[k]
                if k in self.dirCache:
                    del self.dirCache[k]
                self.unwatch(self.handles[k])
                del self.handles[k]
        else:
            self.dirCache = {}
            self.emit(QtCore.SIGNAL('layoutChanged()'))
            #self.reset()
        
    def pathKey(self, path):
        ## This function is very important.
        ## self.createIndex() requires a unique pointer for every item in the tree,
        ## so we must make sure that we keep a list of objects--1 for each item--
        ## since Qt won't protect them for us.
        
        path = os.path.normpath(path)
        if path not in self.paths:
            self.paths[path] = path  ## Index key must be stored locally--Qt won't protect it for us!
            if self.isDir(path):
                self.handles[path] = self.baseDir.getDir(path)
                self.watch(self.handles[path])
            else:
                self.handles[path] = None
        return self.paths[path]
        
    def isDir(self, path):
        return os.path.isdir(os.path.join(self.baseDir.dirName(), path))
        
    def dirChanged(self, path):
        self.clearCache(self.sender().dirName())
        #print "dirChanged:", self.sender(), path
        
    def dirIndex(self, dirName):
        """Return the index for a specific directory relative to its siblings"""
        if isinstance(dirName, DirHandle):
            dirName = dirName.dirName()
            
        if dirName == '' or dirName is None:
            return QtCore.QModelIndex()
        if not self.baseDir.exists(dirName):
            raise Exception("Dir %s does not exist" % dirName)
        row = self.pathRow(dirName)
        return self.createIndex(row, 0, self.pathKey(dirName))
        
    def getFileName(self, index):
        return os.path.join(self.baseDir.dirName(), index.internalPointer())
        
    def findIndex(self, fileName):
        fileName = os.path.normpath(fileName)
        if self.baseDir.dirName() in fileName:
            fileName = fileName.replace(self.baseDir.dirName(), '')
        while len(fileName) > 0 and fileName[0] in ['/', '\\']:
            fileName = fileName[1:]
        return self.dirIndex(fileName)
        
    def index(self, row, column, parent=QtCore.QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()
        if not parent.isValid():
            path = ''
        else:
            path = parent.internalPointer()
        c = self.listdir(path)
        if row >= len(c):
            return QtCore.QModelIndex()
        path = os.path.join(path, c[row])
        pathStr = self.pathKey(path)
        return self.createIndex(row, column, pathStr)
            
    def cmp(self, path, a, b):
        a1 = os.path.join(self.baseDir.dirName(), path, a)
        b1 = os.path.join(self.baseDir.dirName(), path, b)
        aid = os.path.isdir(a1)
        bid = os.path.isdir(b1)
        if aid and not bid:
            return -1
        elif bid and not aid:
            return 1
        else:
            return cmp(a,b)
            
    def listdir(self, path):
        if path not in self.dirCache:
            c = filter(lambda s: s[0] != '.', os.listdir(os.path.join(self.baseDir.dirName(), path)))
            c.sort(lambda a,b: self.cmp(path, a, b))
            self.dirCache[path] = c
        return self.dirCache[path]
        
    def pathRow(self, path):
        #try:
        base, last = os.path.split(os.path.normpath(path))
        c = self.listdir(base)
        return c.index(last)
        #except:
            #print "path", path, "base", base, "last", last
            #raise
            
    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()
        path = os.path.normpath(index.internalPointer())
        base, last = os.path.split(path)
        if base == '/' or base == '':
            return QtCore.QModelIndex()
        pathStr = self.pathKey(base)
        #print "Finding parent of", path, pathStr
        try:
            return self.createIndex(self.pathRow(pathStr), 0, pathStr)
        except:
            return QtCore.QModelIndex()
            
    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            p = ''
        else:
            p = parent.internalPointer()
        p = os.path.normpath(p)
        if not os.path.isdir(os.path.join(self.baseDir.dirName(), p)):
            return 0
        c = self.listdir(p)
        return len(c)
            
    def columnCount(self, index):
        return 1
    
    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        path = os.path.normpath(index.internalPointer())
        base, last = os.path.split(path)
        fullPath = os.path.join(self.baseDir.dirName(), path)
        parent = self.baseDir.getDir(os.path.join(self.baseDir.dirName(), base))
        
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            ret = last
        elif role == QtCore.Qt.TextColorRole:
            if parent.isManaged() and last not in parent.ls():
                ret = QtGui.QColor(100,0,0)
            if os.path.isdir(fullPath):
                ret = QtGui.QColor(0,0,100)
            else:
                ret = QtGui.QColor(0,0,0)
        elif role == QtCore.Qt.BackgroundRole:
            if fullPath == self.currentDir:
                ret = QtGui.QBrush(QtGui.QColor(150, 220, 150))
            else:
                ret = QtCore.QVariant()
        else:
            ret = QtCore.QVariant()
        return QtCore.QVariant(ret)

    def flags(self, index):
        #return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        if index is None:
            return None
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDropEnabled
        path = os.path.normpath(index.internalPointer())
        fullPath = os.path.join(self.baseDir.dirName(), path)
        if os.path.isdir(fullPath):
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled
            
    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant("Files")
        return QtCore.QVariant()
        
    def setData(self, index, value, role):
        if not index.isValid():
            return False
        if role == QtCore.Qt.EditRole:
            newName = str(value.toString())
            if newName == '':
                return False
            base, fn = os.path.split(os.path.normpath(index.internalPointer()))
            #fn = os.path.join(self.baseDir.dirName(), fn)
            #dirName = os.path.split(fn)[0]
            #fn2 = os.path.join(dirName, newName)
            if fn == newName:
                return False
            try:
                dh = self.baseDir.getDir(base)
                
                ## request that the datahandler rename the file so meta info stays in sync
                dh.rename(fn, newName)
                #os.rename(fn, fn2)
                
                self.clearCache(base)
                
                ## Inform anyone interested that the file name has changed
                fn1 = os.path.join(dh.dirName(), fn)
                fn2 = os.path.join(dh.dirName(), newName)
                self.emit(QtCore.SIGNAL('fileRenamed(PyQt_PyObject, PyQt_PyObject)'), fn1, fn2)
                self.emit(QtCore.SIGNAL('dataChanged(const QModelIndex &, const QModelIndex &)'), index, index)
                #print "Data changed, editable:", int(self.flags(index))
                return True
            except:
                print fn, fn2
                sys.excepthook(*sys.exc_info())
                return False
        else:
            print "setData ignoring role", int(role)
            return False

    def supportedDropActions(self):
        return QtCore.Qt.CopyAction | QtCore.Qt.MoveAction

    def supportedDragActions(self):
        return QtCore.Qt.CopyAction | QtCore.Qt.MoveAction

    #def insertRows(self, row, count, parent):
        #print "inasertRows"
        #return False
        
    #def insertColumns(self, column, count, parent):
        #return False

    def dropMimeData(self, data, action, row, column, parent):
        files = str(data.text()).split('\n')
        
        for f in files:
            fn = os.path.join(self.baseDir.dirName(), f)
            if not os.path.exists(fn):
                print "Can not move %s (File does not exist)" % fn
                return False
            if os.path.split(f)[0] == parent.internalPointer():
                print "Can not move %s (Same parent dir)"  % fn
                return False
        try:
            for f in files:
                fullName = os.path.join(self.baseDir.dirName(), f)
                oldDirName, name = os.path.split(f)
                newDirName = parent.internalPointer()
                if newDirName is None:  ## Move to baseDir
                    newDirName = ''
                newName = os.path.join(self.baseDir.dirName(), newDirName, os.path.split(f)[1])
                #os.rename(fullName, newName)
                if action == QtCore.Qt.MoveAction:
                    oldDir = self.baseDir.getDir(oldDirName)
                    newDir = self.baseDir.getDir(newDirName)
                    oldDir.move(name, newDir)
                    #os.rename(fullName, newName)
                    self.emit(QtCore.SIGNAL('fileRenamed(PyQt_PyObject, PyQt_PyObject)'), fullName, newName)
                elif action == QtCore.Qt.CopyAction:
                    os.copy(fullName, newName)
                self.clearCache()
                self.emitTreeChanged(os.path.split(f)[0])
                self.emitTreeChanged(parent.internalPointer())
                self.emit(QtCore.SIGNAL('layoutChanged()'))
            return True
        except:
            sys.excepthook(*sys.exc_info())
            return False
        
    def emitTreeChanged(self, dirName):
        root = self.dirIndex(dirName)
        ch1 = self.index(0,0,root)
        numc = self.rowCount(root)
        ch2 = self.index(numc-1, 0, root)
        #print "emit changed:", dirName, ch1, ch2
        self.emit(QtCore.SIGNAL('dataChanged(const QModelIndex &, const QModelIndex &)'), ch1, ch2)
        
        
    def insertRows(self, row, count, parent):
        #print "Not inserting row"
        return False
        
    def removeRows(self, row, count, parent):
        #print "not removing row"
        return False

    def insertRow(self, row, parent):
        #print "Not inserting row"
        return False
        
    def removeRow(self, row, parent):
        #print "not removing row"
        return False


    def mimeData(self, indexes):
        s = "\n".join([i.internalPointer() for i in indexes])
        m = QtCore.QMimeData()
        m.setText(s)
        return m
        
    def mimeTypes(self):
        return QtCore.QStringList(['text/plain'])
