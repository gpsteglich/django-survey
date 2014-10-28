function OperatorChecks() {
	OperatorList.call();
}

OperatorChecks = Object.create(OperatorList);
OperatorChecks.prototype.constructor = OperatorChecks;

OperatorChecks.contains = function(item, list_str){
	list = list_str.split('#');
	for (var i = 0; i < list.length; i++) {
        if (list[i] === item) {
            return true;
        }
    }
    return false;
}

OperatorChecks.not_contains = function(item, list_str){
	list = list_str.split('#');
	for (var i = 0; i < list.length; i++) {
        if (list[i] === item) {
            return false;
        }
    }
    return true;
}

operatorFactory.registerOperator('CheckboxField', OperatorChecks);
