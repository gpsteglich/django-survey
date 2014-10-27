function OperatorList() {

	OperatorField.call();
}


OperatorList = Object.create(OperatorField);
OperatorList.prototype.constructor = OperatorList;

OperatorList.register = function(){
	//llamar a factory
}

OperatorList.equal = function(a, b){
	return (a === b);
}

OperatorList.not_equal = function(a, b){
	return (a !== b);
}

operatorFactory.registerOperator('SelectField', OperatorList);
