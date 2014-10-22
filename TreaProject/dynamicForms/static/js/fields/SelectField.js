function SelectField() {
	
}

SelectField.buildField = function(){
	var field = FieldBase.buildField(this);
	field.field_type = SelectField.name;
	field.options = [];
    field.max_id = 0;
	return (field);
};

// Register field constructor in Factory
fieldFactory.registerField(SelectField.name, SelectField);
