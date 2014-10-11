function OperatorNumber() {
	OperatorField.call();
}

OperatorNumber = Object.create(OperatorField);
OperatorNumber.prototype.constructor = OperatorNumber;

OperatorNumber.greater_than = function(a, b){
	return (a > b);
}

OperatorNumber.greater_than_or_equal = function(a, b){
	return (a >= b);
}

OperatorNumber.equal = function(a, b){
	return (a == b);
}

OperatorNumber.not_equal = function(a, b){
	return (a != b);
}

OperatorNumber.less_than_or_equal = function(a, b){
	return (a <= b);
}

OperatorNumber.less_than = function(a, b){
	return (a < b);
}

operatorFactory.registerOperator('number', OperatorNumber);
