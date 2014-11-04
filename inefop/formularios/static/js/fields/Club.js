function ClubField() {
	return fieldFactory.getField('ModelField');	
}

// Register field constructor in Factory
fieldFactory.registerField(ClubField.name, ClubField);