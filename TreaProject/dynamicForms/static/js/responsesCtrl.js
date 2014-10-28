(function () {
	
    var app = angular.module('dynamicFormsFramework', []);
    
    /*
     * This controller handles the logic to create, edit and save a form.
     */    
    app.controller('ResponsesCtrl', function ($scope, $http, $location, $window) {

    	var responses = this;
    	responses.formId = ($location.search()).form;
        responses.versionNumber = ($location.search()).ver;
        responses.json = "";

        responses.getResponses = function(){
            $http.get(responses.formId+'/'+ responses.versionNumber+'/')
            .success(function(data){
                responses.json = data;
            })
            .error(function(data, status, headers, config){
                alert(data + status);
            })
        }

        //calls the function getResponses
        responses.getResponses();

    });
})();
