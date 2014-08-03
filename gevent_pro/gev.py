

import gevent

sleep = gevent.sleep

class Gev(object):
	G_thread = []
	G_kv = {}
	@staticmethod
	def spawn(func):

		def _spawn(*arg,**karg):
			counter =  len(Gev.G_thread)
			Gev.G_kv[counter] = gevent.spawn(func,*arg,**karg)
			Gev.G_thread.append(Gev.G_kv[counter])
		
		return _spawn
	
	@staticmethod
	def runAll():
		if len(Gev.G_thread):
			gevent.joinall(Gev.G_thread)
	
	@staticmethod
	def get_value(*keys):
		if not keys:
			return (i.value for i in Gev.G_kv.values())
		return (Gev.G_kv[key].value for key in keys)

	@staticmethod
	def get_handlers(*keys):
		if not keys:
			return (i for i in Gev.G_kv.values())
		return (Gev.G_kv[key] for key in keys)		





