function MatriculaField() {
	
}

MatriculaField.buildField = function(){
	var field = FieldBase.buildField(this);
	field.field_type = MatriculaField.name;
	field.validations = {};
	return (field);
};

// Register field constructor in Factory
fieldFactory.registerField(MatriculaField.name, MatriculaField);