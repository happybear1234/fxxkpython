class Handsomeb:
	def __enter__(self):
		print("进入enter方法")
		return self

	def __exit__(self,type,value,trace):
		print("进入exit方法")
		print("type",type)
		print("value",value)
		print("trace",trace)
		return True
	def cal(self):
		return 100/1

def get_Handsomeb():
	return Handsomeb()

with get_Handsomeb() as h:
	h.cal()