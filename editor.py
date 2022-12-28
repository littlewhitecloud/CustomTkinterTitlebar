from custom import CTT

class Editor(CTT):
	def __init__(self, ):
		super().__init__()
		self.usetitle(False)
		self.w, self.h = 975, 525
		self.geometry("%sx%s" % (self.w, self.h))
		

if __name__ == "__main__":
	example = Editor()
	example.mainloop()
