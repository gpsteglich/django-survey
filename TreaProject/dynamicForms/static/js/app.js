'use strict';

(function () {
    /*
    * Module dynamicForms
    * This module encapsulates the logic that will handle the form.
    */
    var app = angular.module('dynamicForms', []);

    app.controller('VisorCtrl', ['$scope','$http', function ($scope, $http) {
      
       
        
        this.questions = [
            {
                type: 'text',
                text: '¿Cual es tu color favorito?',
                required: true,
                answer: '',
            },
            {
                type: 'number',
                text: '¿Qué edad tenés?',
                required: false,
                answer: '',
            },
            {
                type: 'textarea',
                text: 'Direccion',
                required: false,
                answer: '',
            },
            {
                type: 'number',
                text: 'Número de teléfono',
                required: true,
                answer: '',
            }
        ];
        var visor = this;
//        $http.get('form/13/').success(function(data){
//            
//            visor.form = data;
//            var jsonStr = data.json;
//            jsonStr = jsonStr.replace(/'/gi, '"');
//            jsonStr = jsonStr.replace(/True/gi, 'true');
//            jsonStr = jsonStr.replace(/False/gi, 'false');
//            visor.jsonStr = jsonStr;
//            //descomentar la siguiente linea para usar la api de django
//            visor.questions = JSON.parse(jsonStr);
//            
//            // Keep a copy to check changes
//            visor.orignialQuestions = angular.copy(visor.questions);
//            
//        });
        
      }]);
    
    app.controller('EditorCtrl', ['$scope','$http', function ($scope, $http) {
        this.questions = [
            {
                type: 'text',
                text: '¿Cual es tu color favorito?',
                required: true,
                answer: '',
            },
            {
                type: 'number',
                text: '¿Qué edad tenés?',
                required: false,
                answer: '',
            },
            {
                type: 'textarea',
                text: 'Direccion',
                required: false,
                answer: '',
            },
            {
                type: 'number',
                text: 'Número de teléfono',
                required: true,
                answer: '',
            }
        ];
        
        
        this.selectedField;
      
        this.selectField = function(index) {
            
            this.selectedField = this.questions[index];

        };
        
        this.FieldTypes = [
            'text',
            'number',
            'textarea'            
        ];
        
        this.deleteField = function(index){
        
            this.questions.splice(index,1);        
        };
        
         this.newField =  {
                type:'' ,
                text: '',
                required: '',
                answer: '',
            };
         this.addField = function() {
        
            this.questions.push(angular.copy(this.selectedField));
            this.selectedField = angular.copy(this.newField);

            
        };
       
        
        this.clearSelectedField = function(){
            this.selectedField = angular.copy(this.newField);            
        };
        
    }]);
})();

