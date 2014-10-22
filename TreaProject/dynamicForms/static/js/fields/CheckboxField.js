function CheckboxField() {
	
}

CheckboxField.buildField = function(){
	var field = FieldBase.buildField(this);
	field.field_type = CheckboxField.name;
	field.options = [];
    field.max_id = 0;
	return (field);
};

// Register field constructor in Factory
fieldFactory.registerField(CheckboxField.name, CheckboxField);
