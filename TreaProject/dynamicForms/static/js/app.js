'use strict';

(function () {
    var app = angular.module('dynamicForms', []);

    app.controller('visorCtrl', ['$scope', '$http', function ($scope, $http) {
        /*
        $scope.questions = [
            {
                type: 'text',
                text: '¿Cual es tu color favorito, gil!',
                required: true,
                answer: '',
            },
            {
                type: 'number',
                text: '¿Qué edad tenés?',
                required: false,
                answer: '',
            }
        ];
        */
        $scope.posts = [];
        $http.get('form/4/').success(function(data){
            $scope.form = data;
            var jsonStr = data.json;
            jsonStr = jsonStr.replace(/'/gi, '"');
            jsonStr = jsonStr.replace(/T/, 't');
            jsonStr = jsonStr.replace(/F/, 'f');
            $scope.jsonStr = jsonStr;
            $scope.questions = JSON.parse(jsonStr);
        });        
    } ]);
})();

