import re
from django.core.exceptions import ValidationError


class NumberValidator(object):
	"""
	Validator for numbers, makes sure they are integers.
	"""
	def __call__(self, value):
		try:
			int(value)
		except (ValueError, TypeError):
			raise ValidationError('Enter a valid integer.', code='invalid')


validate_number = NumberValidator()

class IdValidator(object):
	"""
	Validator for Uruguay's id
	"""
	def __call__(self, value):
		value = re.sub('[.-]', '', value)
		try:
			int(value)
		except (ValueError, TypeError):
			raise ValidationError('Enter a valid integer.', code='invalid')

		digits = [int(i) for i in value]
		# If value has less than 8 digits, we complete with zeros on the left
		if len(digits) < 8:
			diff = 8 - len(digits)
			for x in range(0, diff + 1):
				digits.insert(0, 0)
		
		const = [2, 9, 8, 7, 6, 3, 4]
		value = 0
		for x in range(0,7):
			value += digits[x] * const[x]
		m = value % 10
		if ((10 - m) % 10) != digits[len(digits) - 1]:
			raise ValidationError('Enter a valid ID.', code='invalid')

validate_id = IdValidator()