def interview(lst, tot):
	if(len(lst) != 8):
		return'disqualified'
		#não respondeu a quantidade de perguntas nescessárias
	
	if(tot > 120):
		return'disqualified'
		#não respondeu as perguntas no tempo estipulado
		
	for x in range(0, 7):
		if(x < 2):
			if(lst[x] > 5):
				return'disqualified'
				break
				#não respondeu no tempo determinado
		if(x < 4):
			if(lst[x] > 10):
				return'disqualified'
				break
				#não respondeu no tempo determinado
		if(x < 6):
			if(lst[x] > 15):
				return'disqualified'
				break
				#não respondeu no tempo determinado
		if(x < 8):
			if(lst[x] > 20):
				return'disqualified'
				break
				#não respondeu no tempo determinado
	return'qualified'
				
		
print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120) )
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 120) )
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64) )
print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120) )
print(interview([5, 5, 10, 10, 15, 15, 20], 120) )
print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130) )
print(interview([5, 5, 10, 10, 15, 20, 50], 160) )
print(interview([5, 5, 10, 10, 15, 15, 40], 120) )
print(interview([10, 10, 15, 15, 20, 20], 150) )
print(interview([5, 5, 10, 20, 15, 15, 20, 20], 140) )