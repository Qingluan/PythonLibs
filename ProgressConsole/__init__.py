__all__ = [
	"_progressLog",
]


__doc__ = """
	example:

		>import ProgressConsole ##import 
		>a = []
		>def some(box):
		..	for i in range(102):
		..		time.sleep(0.01 * random.randint(0,20))
		..		some = 0
		..		for i in range(random.randint(1000,10000)):
		..			some += i
		..		print some
		..		box.append(some)
		..		yield
		>ProgressConsole.progress.loading("simple",some,a) # you can select "simple" or "default"
	
	run 
		..simple
		.. \87%
"""
from _progressLog import progress