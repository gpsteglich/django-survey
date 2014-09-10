'use strict';

(function () {
    var app = angular.module('dynamicForms', []);

    
    app.controller('visorCtrl', ['$scope', '$http','$window', function ($scope, $http,$window) {
        $scope.selectedField ;
      
        $scope.greeting = 'Hello, World!';
        $scope.selectField = function(index) {
            
            $scope.selectedField = $scope.questions[index];

        };
        
        $scope.FieldTypes = [
            'text',
            'number',
            'textarea'            
        ];

        $scope.miTipo = $scope.FieldTypes[0];
        
        $scope.questions = [
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
//        $scope.posts = [];
//        $http.get('form/13/').success(function(data){
//            $scope.form = data;
//            var jsonStr = data.json;
//            jsonStr = jsonStr.replace(/'/gi, '"');
//            jsonStr = jsonStr.replace(/T/gi, 't');
//            jsonStr = jsonStr.replace(/F/gi, 'f');
//            $scope.jsonStr = jsonStr;
//            //descomentar la siguiente linea para usar la api de django
//            //$scope.questions = JSON.parse(jsonStr);
//            
//            // Keep a copy to check changes
//            $scope.orignialQuestions = angular.copy($scope.questions);
//            
//        });
        // Function to check changes
        $scope.unchanged = function(){
            return angular.equals($scope.questions, $scope.orignialQuestions);   
        };
        $scope.save = function(){
            alert(JSON.stringify($scope.questions));
        };
    }]);
})();

