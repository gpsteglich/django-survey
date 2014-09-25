'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * This controller handles the logic to display the list of forms
     */    
    app.controller('MainPageCtrl', ['$scope','$http', function ($scope, $http) {
    	
    	var mainPage = this;

        //FIXME: corregir la manera de obtener el slug
        var pattern = location.pathname.match(/\/responses\/([\w]*)\/(\w*)/);
        
        mainPage.slug = pattern[1];
        mainPage.ver = pattern[2];

        mainPage.json = [
            {
                "entry_time": "2014-09-25",
                "fields": [
                    "dsdsds : nnnnnnnnnnnnnnnn"
                ]
            },
            {
                "entry_time": "2014-09-25",
                "fields": [
                    "dsdsds : mmmmmmmmmmm"
                ]
            }
        ];
/*
        $http.get('/dynamicForms/responses/'+mainPage.slug+'/'mainPage.ver)
            .success(function(data){
                mainPage.json = data;
            })
            .error(function(data, status, headers, config){
                alert('error cargando respuestas: ' + status);
            })
*/    }]);
})();