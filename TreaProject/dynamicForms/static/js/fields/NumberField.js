function NumberField() {
	
}

NumberField.buildField = function(){
	var field = FieldBase.buildField(this);
	field.field_type = NumberField.name;
	field.validations = {
        min_number: null,
        max_number: null,
    };
	return (field);
};

// Register field constructor in Factory
fieldFactory.registerField(NumberField.name, NumberField);
