function FileField() {
	
}

FileField.buildField = function(){
	var field = FieldBase.buildField(this);
	field.field_type = FileField.name;	
    field.validations = {};
	return (field);
};

// Register field constructor in Factory
fieldFactory.registerField(FileField.name, FileField);