for x in range(20000):
	for y in range(20000):
		for z in range(20000):
			for t in range(20000):
				for u in range(20000):
					if (x*y+z==9535) and (y*x+t==14242) and (z*t+u==5843) and (u*t+z==7113) and (x*u+y==28735):
						print x,y,z,t,u
