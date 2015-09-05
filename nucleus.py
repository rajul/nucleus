class Nucleus(object):
	def __init__(self, atomic_number=1, mass_number=1):
		self.atomic_number = atomic_number
		self.mass_number = mass_number

	def get_nuclear_charge(self):
		pass
		
	def get_num_protons(self):
		return self.atomic_number

	def get_neutral_num_electrons(self):
		return self.atomic_number

	def get_num_neutrons(self):
		return (self.mass_number - self.atomic_number)

	def get_characteristic_x_ray_wavelength(self):
		pass

	def is_same_atom(self, other):
		return (self.atomic_number == other.atomic_number)
				&& (self.mass_number == other.mass_number)

	def is_isotope(self, other):
		return (self.atomic_number == other.atomic_number)
				&& (self.mass_number != other.mass_number)

	def is_isotone(self, other):
		return (self.get_num_neutrons() == other.get_num_neutrons())
				&& (self.atomic_number != other.atomic_number)

	def is_isobar(self, other):
		return (self.atomic_number != other.atomic_number)
				&& (self.mass_number == other.mass_number)

	def get_spin_moment(self, other):
		pass

	def get_orbital_moment(self, other):
		pass

	def get_nuclear_spin(self, other):
		pass

