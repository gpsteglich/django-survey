(function () {
    var app = angular.module('dynamicForms', []);

    app.controller('visorCtrl', ['$scope', '$http', function ($scope, $http) {
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
        /*
        $scope.posts = [];
        $http.get('list').success(function(data){
            $scope.posts = data;
        });
        */
        
        $scope.templates = "question_num"
        
    } ]);
    
})();

