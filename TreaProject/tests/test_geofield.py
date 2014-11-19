import unittest
from dynamicForms.fieldtypes.GeoField import GeoField
from dynamicForms.fieldtypes.FieldFactory import FieldFactory as Factory
from django.core.exceptions import ValidationError


class Test_GeoField(unittest.TestCase):
	
	def setUp(self):
		self.GeoField=(Factory.get_class('GeoField'))()

	def test_tostrig(self):
	 	self.assertEqual(self.GeoField.__str__(),"GeoLocation")

	def test_get_methods(self):
		l=self.GeoField.get_methods()
		self.assertEqual(len(l),2)

	def test_geo_check1(self):
		self.GeoField.geo_check("71#4",field=2)
		self.assertEqual

	def test_geocheck2(self):
		try:
			self.GeoField.geo_check("91#4",field=2)
			self.assertEqual(1,0)
		except:
			self.assertEqual

	def test_geocheck3(self):
		try:
			self.GeoField.geo_check("71#200",field=2)
			self.assertEqual(1,0)
		except:
			self.assertEqual
