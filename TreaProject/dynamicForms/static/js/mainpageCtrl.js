'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * This controller handles the logic to display the list of forms
     */
    app.controller('MainPageCtrl', ['$scope','$http','$location', '$window','$rootScope', 
            function ($scope, $http, $location, $window, $rootScope) {
    	
        //$scope.urlBase = $rootScope.urlBase;

    	var mainPage = this;
        mainPage.formSlugParam = ($location.search()).form;
        mainPage.versionIdParam = ($location.search()).ver;
        mainPage.orders = [
            {name: "Id", value: "id"},
            {name: "Owner", value: "owner"},
            {name: "Title", value: "title"},
            //{name: "Publish Date", value: "publish_date"},
        ]

        mainPage.selectascdsc = function(ascdsc){
            mainPage.ascdsc = ascdsc;
        }

        mainPage.url = function(){
            var parser = $location.absUrl();
            var arr = parser.split('/');
            var crit = arr[arr.length - 3];
            var sent = arr[arr.length - 2];
            return ([crit, sent]);
        }

        //deletes draft version of form
        /* HAS AN ERROR
        mainPage.discardVersion = function(formId, versionNum){
            $http.delete('dynamicForms/version/'+formId+'/'+versionNum)
                .success( function(data, status, headers, config){
                    $window.location.href = '/dynamicForms/main';
                })
                .error(function(data, status, headers, config) {
                    alert('Error discarding version/'+formId+'/'+versionNum + '. Status: ' + status );
                });

        }
        */

        mainPage.actualOrder = function(){
            if (mainPage.url()[0] == 'owner'){
                return mainPage.orders[1];
            } else if (mainPage.url()[0] == 'title'){
                return mainPage.orders[2];
            } else { //default: id
                return mainPage.orders[0];
            }
        }

        if (mainPage.url()[1] == 'dsc'){
            mainPage.selectascdsc('dsc');
            mainPage.actualascdsc = 'DSC';
        } else {
            mainPage.selectascdsc('asc');
            mainPage.actualascdsc = 'ASC';
        }
            
        mainPage.getResponses = function(){
            $http.get('responses/'+mainPage.formSlugParam+'/'+ mainPage.versionIdParam+'/')
            .success(function(data){
                mainPage.json = data;
            })
            .error(function(data, status, headers, config){
                alert('Error loading form data: ' + status);
            })
        }
    }]);
})();
