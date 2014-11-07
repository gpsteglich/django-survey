function UsuarioField() {
	return fieldFactory.getField('ModelField');	
}

// Register field constructor in Factory
fieldFactory.registerField(UsuarioField.name, UsuarioField);