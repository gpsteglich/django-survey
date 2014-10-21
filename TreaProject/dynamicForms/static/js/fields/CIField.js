function CIField() {
	
}

CIField.buildField = function(){
	var field = FieldBase.buildField(this);
	field.field_type = CIField.name;
	return (field);
};

// Register field constructor in Factory
fieldFactory.registerField(CIField.name, CIField);
