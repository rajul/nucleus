class Nucleus(object):
	def __init__(self, atomic_number=1, mass_number=1):
		self.atomic_number = atomic_number
		self.mass_number = mass_number

	def get_nuclear_radius(self):
		pass

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

	def get_spin_moment(self):
		pass

	def get_orbital_moment(self):
		pass

	def get_nuclear_spin(self):
		pass

	def get_electric_quadrupole_moment(self):
		pass

	def get_binding_energy(self, change_in_mass):
		speed_of_light = 3 * 10^8
		return change_in_mass * speed_of_light^2

	def get_binding_energy(self, change_in_energy):
		speed_of_light = 3 * 10^8
		return change_in_energy / speed_of_light^2

	