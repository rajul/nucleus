class Atom(object):
	def __init__(self, atomic_number=1, mass_number=1):
		self.atomic_number = atomic_number
		self.mass_number = mass_number

	def get_number_of_electrons(self):
		return self.atomic_number

	def get_number_of_protons(self):
		return self.atomic_number

	def get_number_of_neutrons(self):
		return (self.mass_number - self.atomic_number)

	def get_mass_of_atom(self):
		pass

	def get_mass_of_nucleus(self):
		pass

	def get_mass_of_electrons(self):
		pass

	def get_bond_energy_of_electron(self):
		# equals 
		# 	c^2 * ((get_mass_of_nucleus + get_mass_of_electrons) - get_mass_of_atom)
		#	13.6 * self.atomic_number^(12.0/5)
		pass