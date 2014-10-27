'use strict';
var validatorFactory = (function () {
 
    // Available validators classes
    var validator = {};
 
    return {
        getValidator: function ( validatorName ) {
            var Validator = validator[validatorName];
            //console.log('se creó una instancia de la clase '+operatorName);
            return Validator;
        },

        registerValidator: function ( validatorName, Validator ) {
            // Register Operator Class
            validator[validatorName] = Validator;
            //console.log('se registro la clase: ' + validatorName);
            return validatorFactory;
        },

        listValidators: function (){
            return validator;
        }

    };
})();

