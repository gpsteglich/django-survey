function SelectField() {
	
}

SelectField.buildField = function(){
	var field = FieldBase.buildField(this);
	field.field_type = SelectField.name;
	field.options = [];
	return (field);
};

// Register field constructor in Factory
fieldFactory.registerField(SelectField.name, SelectField);
