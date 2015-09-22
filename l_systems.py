class L_system(object):

	l_string = []
	rules = dict()
	alphabet = ''

	
	def __init__(self, rule_dict, axiom, abcs):	#dict{str: str}, str, str
		self.l_string = list(axiom)
		self.rules = rule_dict
		self. alphabet = abcs
	
	def successor(self, repetitions=1):		#TODO: implement threading
		new_l_string = []
		
		for l in self.l_string:
			new_l_string.extend(list(self.rules[l]))
		
		self.l_string = new_l_string
		
		r = repetitions - 1

		if r == 0:
			return None 
		return self.successor(r)

	def get_rules(self):
		return self. rules

	def get_alphabet(self):
		return self.alphabet

	def get_l_string(self):
		return self.l_string





