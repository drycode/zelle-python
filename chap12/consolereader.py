class ConsoleReader:
	@staticmethod
	def read_string(prefix):
		""" Read a string from console, with a prefix """
		return input(prefix)

	@staticmethod
	def read_int(prefix, default = None):
		""" Read a (casted) int from console, with a prefix """
		return ConsoleReader.__cast(ConsoleReader.read_string(prefix), int) or default

	@staticmethod
	def read_float(prefix, default = None):
		""" Read a (casted) float from console, with a prefix """
		return ConsoleReader.__cast(ConsoleReader.read_string(prefix), float) or default

	@staticmethod
	def __cast(value, type):
		""" Safely cast a string to another type. """
		parsed = False

		try:
			parsed = type(value)
		except ValueError:
			pass

		return parsed