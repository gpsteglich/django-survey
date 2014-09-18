'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * The VisorCtrl holds the logic to display, validate and submit the form.
     */
    app.controller('VisorCtrl', ['$scope','$http', function ($scope, $http) {

        var visor = this;
        
        /*
         * To get the form the slug is catched form the path.
         * This should be handled by $routerprovider
         */
        var path = location.pathname.match(/\/visor\/(.*)/)[1];
        
        $http.get('/dynamicForms/forms/'+path).success(function(data){            
            visor.form = data;
            visor.questions = JSON.parse(data.json).Fields;
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