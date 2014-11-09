'use strict';
var fieldFactory = (function () {
 
    // Available field classes
    var field = {};
 
    return {
        getField: function ( fieldName ) {
            var Field = field[fieldName];
            //console.log('se creó una instancia de la clase '+fieldName);
            return Field;
        },

        registerField: function ( fieldName, Field ) {
            // Register Field Class
            field[fieldName] = Field;
            return fieldFactory;
        },

        listFields: function (){
            return field;
        }

    };
})();

