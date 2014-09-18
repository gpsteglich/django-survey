'use strict';

(function () {
    app.controller('VisorCtrl', ['$scope','$http', function ($scope, $http) {

        var visor = this;
        
        var path = location.pathname.match(/\/visor\/(.*)/)[1];
        $http.get('/dynamicForms/forms/'+path).success(function(data){            
            visor.form = data;
            var jsonStr = data.json;//          
            visor.jsonStr = jsonStr;
            //descomentar la siguiente linea para usar la api de django
            visor.questions = JSON.parse(jsonStr).Fields;
            
            // Keep a copy to check changes
            visor.orignialQuestions = angular.copy(visor.questions);
            
        });
        
        visor.save = function(){
            $http.post('/dynamicForms/forms/'+visor.form.slug+'/submit/',visor.questions)
                .success( function(data, status, headers, config){
                        
                    })
                .error(function(data, status, headers, config) {
                        alert(status);
                    });
        };
        
        
      }]);
})();