
	
__all__ = [
	"get_words",
	"translator",
]


def get_words(file_name):
	"""
		@write by Qingluan

		it is a iteration 
		just for reading 
	"""
	import re
	for line in open(file_name):
		for word in re.findall(r"[\w'-]+",line):
			yield word


def translator(frm='',to='',delete = '',keep=None):
	"""
		@write by Chris Perkins
		@copy by Qingluan

		a close-block factory
		to deal with some normal string

	"""
	import string


	if len(to)==1:
		to = to * len(frm)
	trans = string.maketrans(frm,to)

	if keep is not None:
		all_chars = string.maketrans('','') # this will get most of chars 
		
		delete = all_chars.translate(allchars,keep.translate(allchars,delete))

	def translate(s):
		return s.translate (trans,delete)
	
	return translate



if __name__ == "__main__":
	import string
	digt_only = translator(keep=string.digits)
	print digt_only('Charis Perkins write this : 2224-7999 #23334-23')
	digits_to_ = translator(frm=string.digits,to='#')
	print digits_to_("Qingluan@ 1026-1142-22")

	trans = translator(keep="Qingluan",delete="luan")
	print trans("Qingluan@ 1026-1142-22")