#Megan Zimmerman
#HW 2 Saving a file
#a simple text editor

from Tkinter import *
from ScrolledText import *
import tkFont
import tkFileDialog
import tkMessageBox
currentName = ""
class Editor(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        #setting the title
        self.parent.title("MegaNotepad")
        menuBar = Menu(self.parent)
        #initializing the menubar into the instance
        self.parent.config(menu=menuBar)
        #initializing a sub menu bar, file menu
        fileMenu = Menu(menuBar)
        fontMenu = Menu(menuBar)
        #adding attributes to file menu bar
        fileMenu.add_command(label="New", command=self.onNew)
        fileMenu.add_command(label="Open", command=self.chooseFileDialog)
        fileMenu.add_command(label="Save", command = self.onNew)
        fileMenu.add_command(label="Save As", command=self.onSaveAs)
        fileMenu.add_command(label="Print", command=self.onNew)
        
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
        fontMenu.add_command(label="Arial",command=self.onArial)
        fontMenu.add_command(label="Times",command=self.onTimes)
        fontMenu.add_command(label="Wingdings",command=self.onWingdings)
        fontMenu.add_command(label="Comic Sans",command=self.onComic)
        #adding the file menu bar into the menu bar
        menuBar.add_cascade(label="File", menu=fileMenu)
        menuBar.add_cascade(label="Font",menu=fontMenu)
        helpMenu = Menu(menuBar)
        helpMenu.add_command(label="About MegaNotepad", command=self.onAbout)
        menuBar.add_cascade(label="Help", menu=helpMenu)

    def chooseFileDialog(self):
        print "choosefile"
        file = tkFileDialog.askopenfile(parent=root,mode='rb', title='Select a file')
        if file != None:
                currentName = file
                contents = file.read()
                textpad.insert('1.0', contents)
                file.close()
    def onArial(self):
        textpad.config(bg = 'white',fg = 'black',font=('Arial', 10, 'normal'))
    def onWingdings(self):
        textpad.config(bg = 'white',fg = 'black',font=('Wingdings', 10, 'normal'))
    def onTimes(self):
        textpad.config(bg = 'white',fg = 'black',font=('Times', 10, 'normal'))
    def onComic(self):
        textpad.config(bg = 'white',fg = 'black',font=('Comic Sans MS', 10, 'normal'))

    def onNew(self):
        print "do new"
    def onSaveAs(self):
        file = tkFileDialog.asksaveasfile(mode='w')
        if file !=None:
            data = textpad.get('1.0',END+'-1c')
            file.write(data)
            file.close()
    def onSave(self):
        return
    def onOpen(self):
        print "do open"
        chooseFileDialog()
        
    def onAbout(self):
        label = tkMessageBox.showinfo("About", "this is a program to read and write .txt files")
    def onExit(self):
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            print "now exiting"
            root.destroy()            

def main():
    global root
    root = Tk()
    global textpad
    textpad = ScrolledText(root, width=100, height =800)
    
    root.geometry("300x200+300+300")
    app = Editor(root)
    textpad.pack()
    root.mainloop()



if __name__ == '__main__':
    main()
            
            
