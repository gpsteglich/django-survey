'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * The PreviewCtrl holds the logic to display a preview of the form
     * with all its functionalities.
     */
    app.controller('PreviewCtrl', ['$scope','$http','$location', function ($scope, $http, $location) {

        var preview = $scope;
        
        /*
        * This controller expects as a query params the form and version to display
        */
        preview.formIdParam = ($location.search()).form;
        preview.versionIdParam = ($location.search()).ver;
        
            // Load Form
        $http.get('forms/'+preview.formIdParam)
            .success(function(data){
                preview.title = data.title;
                 //Load version
                $http.get('version/'+preview.formIdParam+'/'+preview.versionIdParam)
                .success(function(data){
                    preview.version = data;
                    preview.pages = JSON.parse(data.json).pages;
                    preview.selectPage(0);
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
        preview.save = function(){
            alert('Form was completed correctly. \nThis is a preview, the data wont be saved.');   
        }
        
        preview.selectPage = function(page){
            preview.selectedPage = preview.pages[page];
        }
        
        /*
        * The page selection is fired by the change of the url
        */
        preview.changePage = function(page){
            $location.hash(page);
        }

        /*
        * This function watches any change in the url and updates the selected page.
        */
        $scope.$on('$locationChangeSuccess', function(event) {
            var changePage = $location.hash() || 0;
            if (preview.pages){
                if (changePage > preview.pages.size){
                    changePage = 0;   
                }
                preview.selectPage(changePage);
            }
        });
        
    }]);
})();