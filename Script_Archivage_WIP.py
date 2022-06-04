import sys
import os
from PyQt5 import QtGui
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import *
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import shutil
from pathlib import Path


class SceneWindowSource(QWidget):

    submitSrc = qtc.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 300, 100
        self.setMinimumSize(self.window_width, self.window_height) #window minimal size
        self.setWindowTitle('Select Source') #window title

        self.path_src_scene = qtw.QLineEdit()
        self.path_src_scene.setDisabled(True)

        self.path_src_project = qtw.QLineEdit()
        self.path_src_project.setDisabled(True)

        self.path_src_all = qtw.QLineEdit()
        self.path_src_all.setDisabled(True)

        self.cancel_button = qtw.QPushButton('Cancel')
        self.submit_button = qtw.QPushButton('Submit')

        self.setLayout(qtw.QFormLayout())

        self.path_scene = ''
        self.path_project = ''

        btnSc = QPushButton('Search Scene') #create bouton
        btnSc.clicked.connect(self.pickScene)
        self.layout().addWidget(btnSc) #add bouton in layout set-up

        self.layout().addRow('Path:', self.path_src_scene)

        btnProj = QPushButton('Search Project') #create bouton
        btnProj.clicked.connect(self.pickProject)
        self.layout().addWidget(btnProj) #add bouton in layout set-up

        buttons = qtw.QWidget()
        buttons.setLayout(qtw.QHBoxLayout())
        self.layout().addRow('Path:', self.path_src_project)

        buttons.layout().addWidget(self.cancel_button)
        buttons.layout().addWidget(self.submit_button)
        self.layout().addRow('', buttons)

        self.submit_button.clicked.connect(self.on_submit)
        self.cancel_button.clicked.connect(self.close)

    def pickScene(self): #If scene was selected, call windows explorer, pick path and name of selected file
        file_filter = 'Maya scene (*.ma)'
        self.path_scene = QFileDialog.getOpenFileName(
            caption='Select a Scene', #name of the windows explorer's window
            filter=file_filter, #file type that the user can select
            initialFilter='Maya scene (*.ma)'
        )
        self.path_scene = self.path_scene[0]
        print(self.path_scene)
        self.set_messages()

    def pickProject(self): #If scene was selected, call windows explorer, pick path and name of selected file
        self.path_project = QFileDialog.getExistingDirectory(
            caption='Select a Project'
        )
        self.path_project = self.path_project
        print(self.path_project)
        self.set_messages()
    
    def set_messages(self):

        self.path_src_scene.setText(self.path_scene)
        self.path_src_project.setText(self.path_project)
        self.path_src_all.setText(self.path_scene + ' ,' + self.path_project)

    def on_submit(self): #Send information to main window
        self.submitSrc.emit(
            self.path_src_all.text(),
            )
        self.close()

class SQWindowSource(QWidget):

    submitSrc = qtc.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 300, 100
        self.setMinimumSize(self.window_width, self.window_height) #window minimal size
        self.setWindowTitle('Select Source') #window title
        self.setWindowIcon(QtGui.QIcon(r"C:/Users/c.wallez/Desktop/moustache.PNG")) #window icon

        self.path_src_SQ = qtw.QLineEdit()
        self.path_src_SQ.setDisabled(True)

        self.path_src_project = qtw.QLineEdit()
        self.path_src_project.setDisabled(True)

        self.path_src_all = qtw.QLineEdit()
        self.path_src_all.setDisabled(True)

        self.cancel_button = qtw.QPushButton('Cancel')
        self.submit_button = qtw.QPushButton('Submit')

        self.setLayout(qtw.QFormLayout())

        self.path_SQ = ''
        self.path_project = ''

        btnSc = QPushButton('Search SQ') #create bouton
        btnSc.clicked.connect(self.pickSQ)
        self.layout().addWidget(btnSc) #add bouton in layout set-up

        self.layout().addRow('Path:', self.path_src_SQ)

        btnProj = QPushButton('Search Project') #create bouton
        btnProj.clicked.connect(self.pickProject)
        self.layout().addWidget(btnProj) #add bouton in layout set-up

        buttons = qtw.QWidget()
        buttons.setLayout(qtw.QHBoxLayout())
        self.layout().addRow('Path:', self.path_src_project)

        buttons.layout().addWidget(self.cancel_button)
        buttons.layout().addWidget(self.submit_button)
        self.layout().addRow('', buttons)

        self.submit_button.clicked.connect(self.on_submit)
        self.cancel_button.clicked.connect(self.close)

    def pickSQ(self): #If SQ was selected, call windows explorer, pick path and name of selected file
        self.path_SQ = QFileDialog.getExistingDirectory(
            caption='Select a SQ', #name of the windows explorer's window
        )
        self.path_SQ = self.path_SQ
        print(self.path_SQ)
        self.set_messages()

    def pickProject(self): #If SQ was selected, call windows explorer, pick path and name of selected file
        self.path_project = QFileDialog.getExistingDirectory(
            caption='Select a Project'
        )
        self.path_project = self.path_project
        print(self.path_project)
        self.set_messages()
    
    def set_messages(self):

        self.path_src_SQ.setText(self.path_SQ)
        self.path_src_project.setText(self.path_project)
        self.path_src_all.setText(self.path_SQ + ' ,' + self.path_project)

    def on_submit(self): #Send information to main window
        self.submitSrc.emit(
            self.path_src_all.text(),
            )
        self.close()

class ProjectWindowSource(QWidget):

    submitSrc = qtc.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 300, 100
        self.setMinimumSize(self.window_width, self.window_height) #window minimal size
        self.setWindowTitle('Select Project') #window title
        self.setWindowIcon(QtGui.QIcon(r"C:/Users/c.wallez/Desktop/moustache.PNG")) #window icon

        self.src_path_edit = qtw.QLineEdit()
        self.src_path_edit.setDisabled(True)
        self.cancel_button = qtw.QPushButton('Cancel')
        self.submit_button = qtw.QPushButton('Submit')

        self.setLayout(qtw.QFormLayout())

        self.path_src_project = ''

        btn = QPushButton('Search Project') #create bouton
        btn.clicked.connect(self.pickProject)
        self.layout().addWidget(btn) #add bouton in layout set-up

        buttons = qtw.QWidget()
        buttons.setLayout(qtw.QHBoxLayout())
        self.layout().addRow('Path:', self.src_path_edit)
        buttons.layout().addWidget(self.cancel_button)
        buttons.layout().addWidget(self.submit_button)
        self.layout().addRow('', buttons)

        self.submit_button.clicked.connect(self.on_submit)
        self.cancel_button.clicked.connect(self.close)

    def pickProject(self): #If project was selected, call windows explorer, pick path and name of selected folder
        self.path_src_project = QFileDialog.getExistingDirectory(
            caption='Select a Project'
        )
        print(self.path_src_project)
        self.set_messages()

    def set_messages(self):
        self.src_path_edit.setText(self.path_src_project)

    def on_submit(self): #Send information to main window
        self.submitSrc.emit(
            self.src_path_edit.text(),
            )
        self.close()

class WindowDir(QWidget):

    submitDir = qtc.pyqtSignal(str)

    def __init__(self): #Set-Up Window
        super().__init__()
        self.window_width, self.window_height = 300, 100
        self.setMinimumSize(self.window_width, self.window_height) #window minimal size
        self.setWindowTitle('Select Directory') #window title
        self.setWindowIcon(QtGui.QIcon(r"C:/Users/c.wallez/Desktop/moustache.PNG")) #window icon

    #Set_up variable directory path
        self.dst_path_edit = qtw.QLineEdit()
        self.dst_path_edit.setDisabled(True)

    #Set_up buttons link with main window
        self.cancel_button = qtw.QPushButton('Cancel')
        self.submit_button = qtw.QPushButton('Submit')

        self.setLayout(qtw.QFormLayout())

    #Set_up directory search info text
        self.direct_info = qtw.QLineEdit()
        self.direct_info.setDisabled(True)
        self.direct_info.setText('Select Directory')
        self.path_dir = ''

    #create bouton pick directory
        btn = QPushButton('Search') 
        btn.clicked.connect(self.pickDir)
        
        buttons = qtw.QWidget()
        buttons.setLayout(qtw.QHBoxLayout())
        
    #Add widgets to directory window
        self.layout().addWidget(btn)
        self.layout().addRow('Path:', self.dst_path_edit)
        buttons.layout().addWidget(self.cancel_button)
        buttons.layout().addWidget(self.submit_button)
        self.layout().addRow('', buttons)
        self.submit_button.clicked.connect(self.on_submit)
        self.cancel_button.clicked.connect(self.close)
    
    def pickDir(self): #call windows explorer, pick path and name of selected directory
        self.path_dir = QFileDialog.getExistingDirectory( 
            caption='Select a Directory'
        )
        print(self.path_dir)
        self.set_messages()

    def set_messages(self):
        self.dst_path_edit.setText(self.path_dir)

    def on_submit(self): #Send information to main window
        self.submitDir.emit(
            self.dst_path_edit.text(),
            )
        self.close()

class MainWindow(QWidget): #Create Main Window Class
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setFixedWidth(800)

        self.sceneWindow = SceneWindowSource() #Define sceneSourceWindow path 
        self.SQWindow = SQWindowSource() #Define SQSourceWindow path 
        self.ProjectWindow = ProjectWindowSource() #Define ProjectSourceWindow path 

        self.thirdWindow = WindowDir() #Define DirectoryWindow path 

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    #set up variables source and directory path
        self.src_path = ''
        self.dst_path = ''

        self.src_path_display = qtw.QLabel(
            text='waiting for source path',
            font=qtg.QFont('Sans', 10)
            )

        self.dst_path_display = qtw.QLabel(
            text='waiting for directory path',
            font=qtg.QFont('Sans', 10)
            )

        self.options = ('select a scene', 'select a sequence - WIP', 'select a project - WIP') #define options of menu
        self.combo = QComboBox() #create box menu 
        self.combo.addItems(self.options) #add options in menu

    #button call function to open SourceWindow
        self.Confirm_Source = QPushButton('select Source Path') 
        self.Confirm_Source.setStyleSheet('font-size: 15px')
        self.Confirm_Source.clicked.connect(self.openSourceWindow)
        

    #button call function to open directoryWindow
        self.Confirm_Direct = QPushButton('select Directory Path') 
        self.Confirm_Direct.setStyleSheet('font-size: 15px')
        self.Confirm_Direct.clicked.connect(self.openDirectoryWindow)
    
    #button call function to run tout le bordel
        self.Lezgo = QPushButton('LEZGO') 
        self.Lezgo.setStyleSheet('font-size: 15px')
        self.Lezgo.clicked.connect(self.create_All)

    #Add widgets to main window
        self.layout.addWidget(self.src_path_display)
        self.layout.addWidget(self.combo) #add menu in layout set-up
        self.layout.addWidget(self.Confirm_Source)
        self.layout.addWidget(self.dst_path_display)
        self.layout.addWidget(self.Confirm_Direct)
        self.layout.addWidget(self.Lezgo)

    #show Window
        self.show()
    
    def openSourceWindow(self): #Open Source Window
        self.option = self.options.index(self.combo.currentText()) 
        if self.option == 0: #If scene
            self.pickScene()
        elif self.option == 1: #If sequence
            self.pickSQ()
        elif self.option == 2: #If project 
            self.pickProject()
        else:
            print('Got Nothing')
            
    
    def pickScene(self):
        self.sceneWindow.submitSrc.connect(self.update_messages_source)
        self.sceneWindow.set_messages()
        self.sceneWindow.show()

    def pickSQ(self):
        self.SQWindow.submitSrc.connect(self.update_messages_source)
        self.SQWindow.set_messages()
        self.SQWindow.show()

    def pickProject(self):
        self.ProjectWindow.submitSrc.connect(self.update_messages_source)
        self.ProjectWindow.set_messages()
        self.ProjectWindow.show()
    
    def openDirectoryWindow(self): #Open Directory Window
        self.thirdWindow.submitDir.connect(self.update_messages_directory)
        self.thirdWindow.set_messages()
        self.thirdWindow.show()
    
    def create_All(self): 
    #duplicate all hierarchy projet if Project was selected
        self.hierarchy_utl = open(self.dst_path + '\source_hierarchy.txt', 'x')
        self.hierarchy_utl.close()
        self.hierarchy_utl = self.dst_path + '\source_hierarchy.txt'
        
        print(self.src_path)
        
        if self.option == 2:
            self.src_item = self.src_path.rsplit('/', 1)[1]
            print(self.src_item)
            self.dst_item = self.dst_path + '/' + self.src_item
            print(self.dst_item)
            print(self.src_path)
            if not os.path.exists(self.dst_item):
                os.makedirs(self.dst_item)

            with open(self.hierarchy_utl, "w", encoding="utf-8") as filewrite:
                for r, d, f in os.walk(self.src_path):
                    for dirs in d:
                        filewrite.write(f"{r +'/'+ dirs}\n")
        
            with open(self.hierarchy_utl) as f:
                count = sum(1 for _ in f)
                print(count)

            for x in range (0, count):
                with open(self.hierarchy_utl) as f:
                    data = f.readlines()[x]
                    data = data.replace(self.src_path, self.dst_item)
                    data = data.replace('\\', '/')
                    print(data)

                    if not os.path.exists(data):
                        data = data.replace('\n', '')
                        os.makedirs(data)

    #Process if Scene
        if self.option == 0:
            self.src_item = self.src_path.rsplit(',', 1)[1]
            self.scene_path = self.src_path.rsplit(',', 1)[0]
            self.SQ_path = self.src_path.rsplit(',', 1)[0]
            self.src_path = self.src_path.rsplit(',', 1)[1]
            self.src_item = self.src_item.rsplit('/', 1)[1]

            self.scenes_list_utl = open(self.dst_path +'\scenes_list.txt', 'x')
            self.scenes_list_utl.close()
            self.scenes_list_utl = self.dst_path + '\scenes_list.txt'
            
            self.other_list_utl = open(self.dst_path +'\other_list.txt', 'x')
            self.other_list_utl.close()
            self.other_list_utl = self.dst_path + '\other_list.txt'

            writefile = open(self.scenes_list_utl, "a", encoding="utf-8")
            writefile.write("%s\n" % self.scene_path)
            writefile.close()

            self.in_scene_utl = open(self.dst_path + '\in_scene_files.txt', 'x')
            self.in_scene_utl.close()
            self.in_scene_utl = self.dst_path + '\in_scene_files.txt'
            list_all = []
            list_unique = []
            
        #---Write in txt all the path call in the scene file
            with open(self.scene_path) as f:
                self.src_path_l = self.src_path.lower()
                for line in f:
                    line_l = line.lower()
                    if (self.src_path_l) in line_l:
        
                        path_in_scene = line.rsplit('"', 2)[1]

                        list_all.append(path_in_scene)
                        for i in list_all:
                            if i not in list_unique: #if same file call more than one time, juste pick one
                                list_unique.append(i)

            print(list_unique)
            writefile = open(self.in_scene_utl, "a", encoding="utf-8")
            for item in list_unique:
                item = str(item)
                writefile.write("%s\n" % item)
            writefile.close()
            
            print(self.in_scene_utl)
            with open(self.in_scene_utl) as f:
                count = sum(1 for _ in f)
      
        #Separate maya scene and other in two different txt

            list_scene = []
            list_other = []
            for x in range (0, count):
                with open(self.in_scene_utl) as f:
                    data = f.readlines()[x]
                    if not ".ma" in data:
                        list_other.append(data)
                        #print(data)

            #create txt for scenes 
            self.scenes_list_utl = open(self.dst_path +'\scenes_list_1.txt', 'x')
            self.scenes_list_utl.close()
            self.scenes_list_utl = self.dst_path + '\scenes_list_1.txt'
            self.scenes_list_gen_utl = self.dst_path + '\scenes_list.txt'

            writefile = open(self.other_list_utl, "a", encoding="utf-8")
            for item in list_other:
                item = str(item)
                writefile.write("%s\n" % item)
            writefile.close()

            for x in range (0, count):
                with open(self.in_scene_utl) as f:
                    data = f.readlines()[x]
                    if ".ma" in data:
                        list_scene.append(data)

            writefile = open(self.scenes_list_utl, "a", encoding="utf-8")
            for item in list_scene:
                item = str(item)
                writefile.write("%s\n" % item)
            writefile.close()
            
            writefile = open(self.scenes_list_gen_utl, "a", encoding="utf-8")
            for item in list_scene:
                item = str(item)
                writefile.write("%s\n" % item)
            writefile.close()

        #------Same in the all link scene
            hit = 1
            for x in range (1,9):
                with open(self.scenes_list_utl) as f:
                    count = sum(1 for _ in f)
                    #print(count)

                self.scenes_list_utl_x = open(self.dst_path +'\scenes_list_'+ str(x+1) +'.txt', 'x')
                self.scenes_list_utl_x.close()
                self.scenes_list_utl_x = self.dst_path + '\scenes_list_'+ str(x+1) +'.txt'

                for y in range (0, (count-1)):
                    with open(self.scenes_list_utl) as f:
                        data = f.readlines()[y]
                        data = data.replace('\\', '/') 
                        data = data.replace('\n', '')

                        list_all = []
                        list_unique = []

                        if data != "":
                            if '.ma' in data:
                                with open(data) as scenefile:
                                    for line in scenefile:
                                        self.src_path_min = self.src_path.lower()
                                        line_min = line.lower()
                                        if (self.src_path_min) in line_min:
                                            path_in_scene = line.rsplit('"', 2)[1]
                                            #print(path_in_scene)

                                            list_all.append(path_in_scene)
                                            for i in list_all:
                                                if i not in list_unique:
                                                    list_unique.append(i)
                                            #print(list_unique)

                                writefile = open(self.scenes_list_utl_x, "a", encoding="utf-8")
                                for item in list_unique:
                                    item = str(item)
                                    writefile.write("%s\n" % item)
                                writefile.close()
                self.scenes_list_utl = self.scenes_list_utl_x
                hit = hit+1

                test_open = open(self.scenes_list_utl, 'r')
                test_read = test_open.read()
                if test_read == '':
                    break

            list_scene = []
            list_other = []
            print(hit)
            for x in range (2, hit):
                self.scenes_list_utl = self.dst_path + '\scenes_list_'+ str(x) +'.txt'
                print(self.scenes_list_utl)
                
                with open(self.scenes_list_utl) as f:
                        count = sum(1 for _ in f)
                
                for z in range (0, count):
                    with open(self.scenes_list_utl) as f:
                        line = f.readlines()[z]
                        line = line.rstrip('\n')
                        print(line)
                        if not ".ma" in line:
                            list_other.append(line)
                        if ".ma" in line:
                            list_scene.append(line)

                        print(list_scene)
                        print(list_other)

                writefile = open(self.other_list_utl, "a", encoding="utf-8")
                for item in list_other:
                        
                        writefile.write("%s\n" % item)
                writefile.close()

                writefile = open(self.scenes_list_gen_utl, "a", encoding="utf-8")
                for item in list_scene:
                    item = str(item)
                    writefile.write("%s\n" % item)
                writefile.close()
            
        #-------- create Directories 

            self.dst_item = self.dst_path + '/' + self.src_item
            print(self.dst_item)
            path = Path(self.dst_item)
            path.mkdir(parents=True, exist_ok=True)

            list_hierarchy = []
            with open(self.other_list_utl) as f:
                count = sum(1 for _ in f)

            for x in range (0, count):
                with open(self.other_list_utl) as f:
                    line = f.readlines()[x]
                    line = line.rstrip('\n')
                    list_hierarchy.append(line)
                
            with open(self.scenes_list_gen_utl) as f:
                count = sum(1 for _ in f)

            for x in range (0, count):
                with open(self.scenes_list_gen_utl) as f:
                    line = f.readlines()[x]
                    line = line.rstrip('\n')
                    list_hierarchy.append(line)
                
            writefile = open(self.hierarchy_utl, "a", encoding="utf-8")
            for item in list_hierarchy:
                if item != "":
                    item = str(item)
                    print(item)
                    item = item.rsplit('/', 1)[0]
                    print(item)
                    writefile.write("%s\n" % item)
            writefile.close()

            with open(self.hierarchy_utl) as f:
                count = sum(1 for _ in f)
                print(count)

            for x in range (0, count):
                with open(self.hierarchy_utl) as f:
                    path = f.readlines()[x]
                    print(self.src_path)
                    print(self.dst_path)
                    
                    self.src_path_l = self.src_path.lower()
                    o=(path.lower().split(self.src_path_l))
                    c=0
                    p=0
                    for w in o:
                        o[c]=path[p:p+len(w)]
                        p=p+len(self.src_path_l+w)
                        c+=1
                    print(self.dst_item.join(o))
                    path = self.dst_item.join(o)

                    #path = path.replace(self.src_path, self.dst_item)
                    path = path.replace('\\', '/')
                    path = path.replace('//', '/')
                    path = path.rstrip('\n')
                    print(path)
                    path = Path(path)
                    path.mkdir(parents=True, exist_ok=True)

        #-------- copy scenes in news directories                
            
            with open(self.scenes_list_gen_utl, 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                f.writelines(line for line in lines if line.strip())
                f.truncate()     

            with open(self.scenes_list_gen_utl) as f:
                        count = sum(1 for _ in f)
                        print(count)

            for x in range (0, count):
                with open(self.scenes_list_gen_utl, "r", encoding="utf-8") as f:
                    old_scene = f.readlines()[x]
 
                    self.src_path_l = self.src_path.lower()
                    o=(old_scene.lower().split(self.src_path_l))
                    c=0
                    p=0
                    for w in o:
                        o[c]=old_scene[p:p+len(w)]
                        p=p+len(self.src_path_l+w)
                        c+=1
                    print(self.dst_item.join(o))
                    new_scene = self.dst_item.join(o)

                    #new_scene = old_scene.replace(self.src_path, self.dst_item)
                    new_scene = new_scene.replace('\\', '/')
                    data_src=old_scene.replace('\\', '/')
                    print(self.src_path)
                    print(self.dst_item)
                    print(new_scene)
                    print(old_scene)
                    if not os.path.exists(new_scene):
                        data_src = data_src.replace('\n', '')
                        data_dest = new_scene.replace('\n', '')
                        shutil.copyfile(data_src, data_dest)

        #--------- repath all in scenes
                        temp = self.dst_item+'scene_temp.txt'
                        scene_temp = open(temp, 'a')
                        self.test = 0
                        with open(data_dest, 'r') as f:
                            line=''
                            while True:
                                robert = f.read(1)
                                if not robert:
                                    break
                                if robert == '\n':
                                    line+= robert
                                    test_line_l = line.lower()
                                    src_path_l = self.src_path.lower()
                                    if src_path_l in test_line_l:
                                        self.test = self.test+1
                                    line = ''
                                else:
                                    line += robert
                        
                        scene_temp.close()
                        os.remove(temp)

                        print(self.test)
                        if self.test > 0:
                            scene_temp = open(temp, 'a')
                            with open(data_dest, 'r') as f:
                                line=''
                                while True:
                                    robert = f.read(1)
                                    if not robert:
                                        scene_temp.write(line)
                                        break
                                    if robert == '\n':
                                        line += robert

                                        src_path_l = self.src_path.lower()
                                        o=(line.lower().split(src_path_l))
                                        c=0
                                        p=0
                                        for w in o:
                                            o[c]=line[p:p+len(w)]
                                            p=p+len(src_path_l+w)
                                            c+=1
                                        file_lines = self.dst_item.join(o)
                                            
                                        scene_temp.write(file_lines)
                                        line = ''
                                    else:
                                        line += robert
                            scene_temp.close()

                            scene_temp = open(temp, 'r')
                            contenu = scene_temp.read()
                            scene_temp.close()

                            scene=open(data_dest, 'w')
                            scene.write(contenu)
                            scene.close()
                            scene_temp.close()

                            os.remove(temp)

        #-------- copy files in news directories 
            

            with open(self.other_list_utl, 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                f.writelines(line for line in lines if line.strip())
                f.truncate() 

            with open(self.other_list_utl) as f:
                count = sum(1 for _ in f)

            list_all_l = []
            list_unique_l = []
            list_unique = []
            for x in range (0, count):
                with open(self.other_list_utl, 'r+', encoding="utf-8") as f:
                    other_item = f.readlines()[x]
                    print(other_item)
                    other_item = other_item.rsplit('/', 1)[0]
                    print(other_item)
                    other_item_l = other_item.lower()
                    print(other_item_l)
                    list_all_l.append(other_item_l)
                    for i in list_all_l:
                        if i not in list_unique_l:
                            list_unique_l.append(i)
                            list_unique.append(other_item)


            write_other = open(self.other_list_utl, 'w')
            for item in list_unique:
                item = str(item)
                write_other.write("%s\n" % item)
            write_other.close()

            with open(self.other_list_utl, 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                f.writelines(line for line in lines if line.strip())
                f.truncate()


            with open(self.other_list_utl) as f:
                    count = sum(1 for _ in f)
                    print(count)

            for x in range (0, count):
                with open(self.other_list_utl, "r", encoding="utf-8") as f:
                    #old_item = f.readlines()[x]
                    old_dest = f.readlines()[x]
                    #old_dest = old_item.rsplit('/', 1)[0]
                    new_dest = old_dest.replace(self.src_path, self.dst_item)
                    new_dest = new_dest.replace('\\', '/')
                    new_dest = new_dest.replace('//', '/')
                    print(new_dest)
                    print(old_dest)
                    print(self.src_path)
                    print(self.dst_item)

                    src_path_l = self.src_path.lower()
                    src_path_l=src_path_l.replace('\\', '/')
                    src_path_l=src_path_l.replace('//', '/')
                    old_dest_l = old_dest.lower()
                    old_dest_l=old_dest_l.replace('\\', '/')
                    old_dest_l=old_dest_l.replace('//', '/')
                    o=(old_dest_l.split(src_path_l))
                    c=0
                    p=0
                    for w in o:
                        o[c]=old_dest[p:p+len(w)]
                        p=p+len(self.src_path+w)
                        c+=1

                    new_dest=self.dst_item.join(o)
                    
                    print(new_dest)
                    print(old_dest)

                    old_dest = old_dest.replace('\n', '')
                    new_dest = new_dest.replace('\n', '')
                    '''old_dest=old_dest.replace('\\', '/')
                    old_dest=old_dest.replace('//', '/')
                    new_dest=new_dest.replace('\\', '/')
                    new_dest=new_dest.replace('//', '/')'''

                    files = os.listdir(old_dest)
                    
                    for fname in files:
                        print (fname)
                        file_path = old_dest + '/' + fname
                        print(file_path)
                        isFile = os.path.isfile(file_path)
                        print (isFile)
                        if isFile == True:
                            shutil.copy2(os.path.join(old_dest,fname), new_dest)

                    '''for item in os.listdir(old_dest):
                        print(item)
                        s = os.path.join(old_dest, item)
                        print(s)
                        d = os.path.join(new_dest, item)
                        print(d)
                        if os.path.isdir(s):
                            shutil.copytree(s, d)'''

                    '''src_files = os.listdir(old_dest) 
                    for file_name in src_files: 
                        full_file_name = os.path.join(old_dest, file_name)
                
                        print(full_file_name)
                        print(new_dest)
                        
                        if os.path.isfile(full_file_name):
                            shutil.copy(full_file_name, new_dest)'''

    #Copy Files if SQ ------ WIP
        if self.option == 1:
            self.scene_utl = open(self.dst_path + '\source_SQ_scenes.txt', 'x')
            self.scene_utl.close()
            self.scene_utl = self.dst_path + '\source_SQ_scenes.txt'
            list_other=[]
            self.other_utl = self.dst_path + '\source_SQ_other.txt'
            print(self.SQ_path)
            print(self.src_path)

            with open(self.scene_utl, "w", encoding="utf-8") as filewrite:
                for r, d, f in os.walk(self.SQ_path):
                    for file in f:
                        print(file)
                        if ".ma" in file:
                            print(file)
                            if not ".swatches" in file:
                                filewrite.write(f"{r +'/'+ file}\n")
                                print(file)
                            else: 
                                list_other.append(file)
                                print(file)

            with open(self.other_utl, "a", encoding="utf-8") as filewrite:
                for item in list_other:
                    item = str(item)
                    filewrite.write("%s\n" % item)

                        
    #Copy Files if Project 
        if self.option == 2:

            self.file_utl = open(self.dst_path + '\source_files.txt', 'x')
            self.file_utl.close()
            self.file_utl = self.dst_path + '\source_files.txt'
 
            with open(self.file_utl, "w", encoding="utf-8") as filewrite:
                for r, d, f in os.walk(self.src_path):
                    for file in f:
                        filewrite.write(f"{r +'/'+ file}\n")
        
            with open(self.file_utl) as f:
                count = sum(1 for _ in f)
                print(count)

            for x in range (0, count):
                with open(self.file_utl, "r", encoding="utf-8") as f:
                    data = f.readlines()[x]
                    data_dest = data.replace(self.src_path, self.dst_item)
                    data_dest = data_dest.replace('\\', '/')
                    print(data_dest)
                    print(data)
                    print(self.src_path)
                    print(self.dst_item)
                    data=data.replace('\\', '/') 
                    if not os.path.exists(data_dest):
                        data = data.replace('\n', '')
                        data_dest = data_dest.replace('\n', '')
                        shutil.copyfile(data, data_dest)   

        #-------------- Repath                    
                        if ".ma" in data_dest:
                            if not ".swatches" in data_dest:
                                temp = self.dst_item+'scene_temp.txt'
                                scene_temp = open(temp, 'a')
                                with open(data_dest) as f:
                                    count = sum(1 for _ in f)
                                    print(count)
                                for x in range (0, count):
                                    with open (data_dest) as test:
                                        test_line = test.readlines()[x]
                                        test_line_l = test_line.lower()
                                        src_path_l = self.src_path.lower()
                                        test = 0
                                        if src_path_l in test_line_l:
                                            test = test+1

                                print(test)
                                if test > 0:
                                    for x in range (0, count):
                                        with open(data_dest, 'r') as f:
                                            line = f.readlines()[x]

                                            src_path_l = self.src_path.lower()
                                            o=(line.lower().split(src_path_l))
                                            c=0
                                            p=0
                                            for w in o:
                                                o[c]=line[p:p+len(w)]
                                                p=p+len(src_path_l+w)
                                                c+=1
                                            file_lines = self.dst_item.join(o)
                                            
                                            scene_temp.write(file_lines)

                                    scene_temp.close

                                    scene_temp = open(temp, 'r')
                                    contenu = scene_temp.read()
                                    scene_temp.close()

                                    scene=open(data_dest, 'w')
                                    scene.write(contenu)
                                    scene.close()
                                    scene_temp.close()

                                    os.remove(temp)



    #Update Source path in main window
    @qtc.pyqtSlot(str) 
    def update_messages_source(self, source):
        self.src_path = source
        self.src_path_display.setText(self.src_path)
            

    #Update Directory path in main window
    @qtc.pyqtSlot(str) 
    def update_messages_directory(self, directory):
        self.dst_path = directory
        self.dst_path_display.setText(self.dst_path)
    

    def showwindow(self): #show Mainwindow
        self.show()
        try:
            sys.exit(app.exec_())
        except SystemExit:
            print('Closing Window...')

if __name__ == '__main__': #Main Window Class End
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec())