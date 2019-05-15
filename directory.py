from file import File
from sett import Sett

class Directory():
	def __init__(self, name, contentS):
		self.name = name
		self.parent = None
		self.contentS = contentS

	def setParent(self, parent):
		self.parent = parent
	def addContent(self, content):
		self.contentS.append(content)

	def rmContent(self, content):
		self.contentS.pop(self.contentS.index(content))
	
	def whichFile(self, fileName):
		for content in self.contentS:
			if content.__class__.__name__ == 'File' and content.name == fileName:
				return content

	def ls(self):
		for content in self.contentS:
			print(content.name)

	def lsRecursive(self, stemDir):
		currentDir = stemDir + '/' + self.name
		for content in self.contentS:
			print(currentDir + '/' + content.name)
			if content.__class__.__name__ == 'File':
				pass

			elif content.__class__.__name__ == 'Directory':
				content.lsRecursive(currentDir)
			else:
				raise ValueError('wrong!')



