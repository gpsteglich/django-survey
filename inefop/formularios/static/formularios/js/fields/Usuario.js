function UsuarioField() {

}

UsuarioField.buildField = function(){
	var field = FieldBase.buildField(this);
	field.field_type = UsuarioField.name;
	field.options = [];
    field.max_id = 0;
	return (field);
};

// Register field constructor in Factory
fieldFactory.registerField(UsuarioField.name, UsuarioField);