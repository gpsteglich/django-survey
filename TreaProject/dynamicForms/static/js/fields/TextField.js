function TextField() {
	
}

TextField.buildField = function(){
	var field = FieldBase.buildField(this);
	field.field_type = TextField.name;
	field.validations = {
        max_len_text: 255,
    };
	return (field);
};

// Register field constructor in Factory
fieldFactory.registerField(TextField.name, TextField);
