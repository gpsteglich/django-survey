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


        $http.get('/dynamicForms/responses/'+mainPage.slug+'/'+ mainPage.ver+ '/d')
            .success(function(data){
                mainPage.json = data;
            })
            .error(function(data, status, headers, config){
                alert('error cargando respuestas: ' + status);
            })
    }]);
})();
