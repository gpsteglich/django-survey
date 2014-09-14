'use strict';

(function () {
    /*
    * Module dynamicForms
    * This module encapsulates the logic that will handle the form.
    */
    var app = angular.module('dynamicForms', []);

    app.controller('VisorCtrl', ['$scope','$http', function ($scope, $http) {
      
       
        
//        this.questions = [
//            {
//                type: 'text',
//                text: '¿Cual es tu color favorito?',
//                required: true,
//                answer: '',
//            },
//            {
//                type: 'number',
//                text: '¿Qué edad tenés?',
//                required: false,
//                answer: '',
//            },
//            {
//                type: 'textarea',
//                text: 'Direccion',
//                required: false,
//                answer: '',
//            },
//            {
//                type: 'number',
//                text: 'Número de teléfono',
//                required: true,
//                answer: '',
//            }
//        ];
        var visor = this;
        $http.get('forms/form/').success(function(data){
            
            visor.form = data;
            var jsonStr = data.json;//          
            visor.jsonStr = jsonStr;
            //descomentar la siguiente linea para usar la api de django
            visor.questions = JSON.parse(jsonStr).Fields;
            
            // Keep a copy to check changes
            visor.orignialQuestions = angular.copy(visor.questions);
            
        });
        
      }]);
    
    app.controller('EditorCtrl', ['$scope','$http', function ($scope, $http) {
        $scope.editorMode = true; 
//        this.questions = [
//            {
//                type: 'text',
//                text: '¿Cual es tu color favorito?',
//                required: true,
//                answer: '',
//            },
//            {
//                type: 'number',
//                text: '¿Qué edad tenés?',
//                required: false,
//                answer: '',
//            },
//            {
//                type: 'textarea',
//                text: 'Direccion',
//                required: false,
//                answer: '',
//            },
//            {
//                type: 'number',
//                text: 'Número de teléfono',
//                required: true,
//                answer: '',
//            }
//        ];
//        
        //indica el campo seleccionado cuando. cuando doy click se llama a la funcion selectField.
        // se usa en la pestania de modificacion.
        this.selectedField;
      
        this.selectField = function(index) {
            
            this.selectedField = this.questions[index];

        };
        //array de tipos de campos
        this.FieldTypes = [
            'text',
            'number',
            'textarea'            
        ];
        
        this.deleteField = function(index){
            //funcion para eliminar campos, index, es el indice de ng-repeat.
            this.questions.splice(index,1);        
        };
         //modelo de nuevo campo vacio. Falta agregar id a cada campo.
         this.newField =  {
                type:'' ,
                text: '',
                required: '',
                answer: '',
            };
         this.addField = function(type) {
            //se aplica en cada boton de la paleta.
             //type es un tipo del array newField 
             // necesita haber una estructura de array
             // para agregar. Por ej, en modo edicion el array ya viene dado.
             // en modo creacion, se necesita crear una estructura inicial vacia.
             // cuidado con los modelos. Es necesario copiar los modelos, sino seguiran con el binding y se 
             //seguiran modificando.
            var newField = angular.copy(this.newField);
            newField.type = type;
            this.questions.push(newField);
            this.selectedField = angular.copy(this.newField);

            
        };
       
        2
        this.clearSelectedField = function(){
            this.selectedField = angular.copy(this.newField);            
        };
        
        var visor = this;
        //LO MAS PROBABLE ES QUE NO SE MUESTRE UN FORM
        // CAMBIAR form10 POR UN SLAG DE UN FORMULARIO EN TU BASE DE DATOS.
         $http.get('forms/form10/').success(function(data){
            
            visor.form = data;
            var jsonStr = data.json;            
            visor.jsonStr = jsonStr;
            //descomentar la siguiente linea para usar la api de django
            visor.questions = JSON.parse(jsonStr).Fields;
            
            // Keep a copy to check changes
            visor.orignialQuestions = angular.copy(visor.questions);
            
        });
        
        this.submitForm = function(){
            //Esta funcion se llama en el submit del editor. Se puede cambiar el boton por un "guardar formulario en creacion y seguir editando".
//            var newJson = {};
//            newJson["Fields"] = visor.questions;
            
//            visor.form.json =  newJson;
            
            //Se guarda, pero el json NO!!! Probe poner el JSON como string y nada, y a lo ultimo como 
            //como json json y tampoco.
            //post no tengo permisos :S
            //creo que igual se pueden crear forms con put, pero ya digo
            // el json no se guarda...
            //si voy al admin y lo escribo funciona...el tema es la api rest.
            var form = {
                "title": "5",
                "slug": "5",
                "status": 0,
                "publish_date": "2014-09-01",
                "expiry_date": "2014-11-04",
                "version": 1,
                "owner": "federico",
                "json": {"text":"bien"}
            };
            $http.put('forms/21/',form).success( function(data){
                    alert(data);
                    alert('bien');               
                }).error(function() {
                    alert('TODO MAL');
                });        
            };
        
    }]);
})();

