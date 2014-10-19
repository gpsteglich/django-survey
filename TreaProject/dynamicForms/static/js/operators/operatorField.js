function OperatorField() {

}

OperatorField.listMethods = function() {
	var methods = [];
	for (var key in this) {
		if (typeof this[key] === "function" &&
			key != "constructor" && key != "register" && key != "listMethods") {
			methods.push(key);
    	}
	}
	return methods;
}