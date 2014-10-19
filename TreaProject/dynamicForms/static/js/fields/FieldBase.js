function FieldBase() {

}

FieldBase.buildField = function() {
    console.log('buildField Base');
	var field =  {
    	field_id : 0,
        field_type:'' ,
        text: '',
        answer: [],
        validations: {},
        required: false,
        tooltip:'',
        dependencies: {
            fields: [],
            pages: [],
        }
    };
	return field;
};
