
import sys
import time,random

class progress(object):
	"""
		@write by Qingluan

		style can select "simple" or "default"


	"""
	status = {
		0 : '-> \\',
		1 : '-> |',
		2 : '-> /',
		3 : '-> -',
	}
	style = {
		'default' : '#',
		'simple' : '',
	}
	def __init__(self,tag = 0,style="default"):
		self.tag = tag
		self.style = progress.style[style]
		self.status = progress.status[self.tag]
		self.string = self.status + "\b\b\b\b\b"

	def _load(self,i):
		sys.stdout.write(self.string)
		sys.stdout.flush()
		self._count(i)
		
	def _count(self,i):
		self.tag = (self.tag + 1) %4
		if (i!= 100):
			self.string = self.style +progress.status[self.tag] +"%2d%s\b\b\b\b\b\b\b"%(i,'%')
		else:
			self.string = "\r ok "
	def __call__(self):
		for i in range(102):
			self._load(i)
			yield

	@classmethod
	def loading(cls,style,iterable_func,*args,**karg):
		print style
		progresser = cls(tag=0,style=style)
		iteration = iterable_func(*args,**karg)
		for step in progresser():
			iteration.next()
		iteration.close()
			 		
if __name__ =="__main__":
	a = []
	def some(box):
		for i in range(102):
			time.sleep(0.01 * random.randint(0,20))
			some = 0
			for i in range(random.randint(1000,10000)):
				some += i
			box.append(some)
			yield

	progress.loading(some,a)
	
