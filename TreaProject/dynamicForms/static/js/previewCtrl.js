'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * The PreviewCtrl holds the logic to display a preview of the form
     * with all its functionalities.
     */
    app.controller('PreviewCtrl', ['$scope','$http','$location', function ($scope, $http, $location) {

        var preview = this;
        
        /*
        * This controller expects as a query params the form and version to display
        */
        preview.formIdParam = ($location.search()).form;
        preview.versionIdParam = ($location.search()).ver;
        
            // Load Form
        $http.get('forms/'+preview.formIdParam)
            .success(function(data){
                preview.form = data;
                 //Load version
                $http.get('version/'+preview.formIdParam+'/'+preview.versionIdParam)
                .success(function(data){
                    preview.version = data;
                    preview.questions = JSON.parse(data.json).Fields

                })
                .error(function(data, status, headers, config){
                    alert('error loading version: ' + status);
                })
            })
            .error(function(data, status, headers, config){
                alert('error loding form: ' + status);
            })
        
        /*
        * TODO: Sería útil permitir al editor ingresar datos y que sean validados por el back
        * pero sin persistirlos en la base.
        */
        
    }]);
})();