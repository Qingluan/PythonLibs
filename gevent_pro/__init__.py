from __future__ import absolute_import
import time
__all__ = [
	'gev'
]



if __name__ == "__main__":
	test_value = [i for i in xrange(10000000)]
	from gev import Gev
	import gev

	start = time.time()
	
	@Gev.spawn
	def test(arg):
		start = time.time()
		# gev.sleep()
		# print ("finished ")
		all_v = reduce(lambda x,y: x+y ,arg)
		
		return all_v

	count = 0
	for i in range(0,10000000,10000):
		test(test_value[count:i])
		count = i

	Gev.runAll()
	res =  Gev.get_value()
	def la(a,b):
		if not a:
			a = 0
		if not b :
			b = 0
		return a+b

	resv = reduce(la,res)
	end = time.time() - start 
	print (resv,"  pass :",end)



