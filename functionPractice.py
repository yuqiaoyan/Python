def add(a,b):
	return(a,b)

#add becomes a global object that other functions can utilize

def test(fn):
	if(fn == add):
		print fn(3,5)

#i can pass add to test and get 3+5

test(add)
