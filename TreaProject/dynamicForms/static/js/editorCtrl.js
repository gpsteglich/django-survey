'use strict';

(function () {
    var app = angular.module('dynamicFormsFramework');
    app.controller('EditorCtrl', ['$scope','$http', function ($scope, $http) {
        $scope.editorMode = true; 
        var editor = this;
        //indica el campo seleccionado cuando. cuando doy click se llama a la funcion selectField.
        // se usa en la pestania de modificacion.
        editor.selectedField;
        editor.questions = [];
        editor.selectField = function(index) {
            
            editor.selectedField = editor.questions[index];

        };
        //array de tipos de campos
        editor.FieldTypes = [
            'text',
            'number',
            'textarea'            
        ];

        editor.deleteField = function(index){
            //funcion para eliminar campos, index, es el indice de ng-repeat.
            editor.questions.splice(index,1);        
        };
         //modelo de nuevo campo vacio. Falta agregar id a cada campo.
         editor.newField =  {
                field_id : 0,
                field_type:'' ,
                text: '',
                required: false,
                answer: '',
            };
         editor.addField = function(type) {
            //se aplica en cada boton de la paleta.
             //type es un tipo del array newField 
             // necesita haber una estructura de array
             // para agregar. Por ej, en modo edicion el array ya viene dado.
             // en modo creacion, se necesita crear una estructura inicial vacia.
             // cuidado con los modelos. Es necesario copiar los modelos, sino seguiran con el binding y se 
             //seguiran modificando.
            var newField = angular.copy(editor.newField);
            newField.field_id = editor.questions.length;
            newField.field_type = type || 'text';
            editor.questions.push(newField);
            editor.selectedField = angular.copy(editor.newField);

            
        };
       
        editor.clearSelectedField = function(){
            editor.selectedField = angular.copy(editor.newField);            
        };
        
        editor.actualSlug;
        if (editor.actualSlug){
             $http.get('forms/'+editor.actualSlug).success(function(data){

                editor.form = data;
                editor.actualSlug = data.slug;
                var jsonStr = data.json;            
                editor.jsonStr = jsonStr;
                editor.questions = JSON.parse(jsonStr).Fields;

            });
        } else {
            editor.form = {
                'title' : '',
                'slug' : '',
                'status' : 1,
                'publish_date' : '2014-06-06',
                'expiry_date' : '2014-06-06',
                'version' : 0,
                'owner' : '',
                'json' : ''
            };
        };
        
       
        editor.submitForm = function(){
//Esta funcion se llama en el submit del editor. Se puede cambiar el boton por un "guardar formulario en creacion y seguir editando".
//            newJson["Fields"] = visor.questions;
            editor.form.json = JSON.stringify({'Fields' : editor.questions});
            if (editor.actualSlug){
                $http.put('forms/'+ editor.actualSlug,editor.form)
                    .success( function(data, status, headers, config){
                        
                        })
                    .error(function(data, status, headers, config) {
                            
                        });
            } else {
                editor.form.slug = 'temp_slug';
                $http.post('forms/',editor.form)
                .success( function(data, status, headers, config){
                        editor.form.slug = data.slug;
                        editor.actualSlug = data.slug;    
                    })
                .error(function(data, status, headers, config) {
                        
                    });
            };
        };
        
    }]);
    
})()