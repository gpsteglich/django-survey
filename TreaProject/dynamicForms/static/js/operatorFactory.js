'use strict';
var operatorFactory = (function () {
 
    // Available operators classes
    var operator = {};
    var operatorMethods = {};
 
    return {
        getOperator: function ( operatorName ) {
            var Operator = operator[operatorName];
            console.log('se creó una instancia de la clase '+operatorName);
            return Operator;
        },
 
        getOperatorMethods: function( operatorName){
            return operatorMethods[operatorName];
        },

        registerOperator: function ( operatorName, Operator ) {
            // Register Operator Class
            // console.log('Operator: ' + Operator.toSource());
            operator[operatorName] = Operator;
            // Register Operator's available methods
            operatorMethods[operatorName] = Operator.listMethods();
            console.log('se registro la clase: ' + operatorName);
            return operatorFactory;
        },

        listOperators: function (){
            return operator;
        }

    };
})();

