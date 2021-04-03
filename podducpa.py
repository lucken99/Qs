class Person:
	def __init__(self, name="", height=0, weight=0):
		self.name = name
		self.height = height
		self.weight = weight
		self.bmi = 0
		self.bmi_status = ""

	def calculateBmi(self):
		bmi = round(self.weight/(self.height*self.height))
		self.bmi = bmi
class Society(Person):
	def __init__(self, bmi_status, person_list):
		self.bmi_status = bmi_status
		self.person_list = person_list

	def calculateBmiAndStatusByName(self, name):
		for i in self.person_list:
			if i.name.lower() == name.lower():
				i.bmi = i.calculateBmi()
				for k,v in self.bmi_status.items():
					if v[0] <= i.bmi <= v[1]:
						i.bmi_status = k
				return True
		return False

	def removeInvalidPersons(self, bmi_val):
		ans = []
		for i in self.person_list:
			if i.bmi < bmi_val:
				ans.append(i.name)

		return ans

if __name__ == '__main__':
	n_list = int(input())
	l_of_person = []
	for i in range(n_list):
		name = input()
		height = int(input())
		weight = int(input())
		l_of_person.append(Person(name, height, weight))

	n_key = int(input())
	d = {}
	for i in range(n_key):
		status = input()
		low = int(input())
		upper = int(input())
		d[status] = (min(low, upper), max(low, upper))
	s_obj = Society(d, l_of_person)
	sec_last = input()
	final_ans = s_obj.calculateBmiAndStatusByName(sec_last)
	if final_ans:
		for i in l_of_person:
			if i.name.lower() == sec_last.lower():
				if i.bmi != 0:
					print(i.bmi)
				print(i.bmi_status)
		
	else:
		print("No Person Exists")

	last = int(input())
	final_ans2 = s_obj.removeInvalidPersons(last)
	for i in final_ans2:
		print(i)
	
	




