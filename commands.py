from sett import Sett
from directory import Directory
from file import File


class CommandS():
    @staticmethod
    def getCwd():
        result = ''
        for dir in Sett.path:
            result += dir.name + '/'
        return result


    @staticmethod
    def pwd():
        print(CommandS.getCwd())

    @staticmethod
    def ls():
        Sett.currentDir.ls()

    def ls_R():
        Sett.currentDir.lsRecursive('')

   

    @staticmethod
    def cd(dirName):

        if dirName == '..' and Sett.currentDir.name is not Sett.rootDir:  # ~ is the root directory, can't go up anymore
            Sett.currentDir = Sett.currentDir.parent
            Sett.path.pop()
            

        for dir in Sett.currentDir.contentS:
            if dir.name == dirName:
                Sett.currentDir = dir
                Sett.path.append(dir)

    @staticmethod
    def mkdir(dirName):
        newDir = Directory(dirName, [])
        newDir.setParent(Sett.currentDir)
        Sett.currentDir.addContent(newDir)
        

    @staticmethod
    def touch(fileName):
        Sett.currentDir.addContent(File(fileName, ''))
    
    @staticmethod
    def rm(contentName):

        for content in Sett.currentDir.contentS:
            if content.name == contentName and content.__class__.name == 'File':
                Sett.currentDir.rmContent(content)
                break
    
    @staticmethod
    def whoami():
        print(Sett.userName)
    
    @staticmethod
    def hostname():
        print(Sett.hostName)
    
    @staticmethod
    def treepad(fileName):
        file = Sett.currentDir.whichFile(fileName)
        file.text = input('>')

    @staticmethod
    def cat(fileName):
        Sett.currentDir.whichFile(fileName).cat()
    
    @staticmethod
    def python():
        import subprocess as sbp
        sbp.call('python', shell=True)
    
    @staticmethod
    def exeunt():
        import sys
        sys.exit()