'use strict';

(function () {
    /*
    * Module dynamicFormsFramework
    * This module encapsulates the logic that will handle the form.
    */
    var app = angular.module('dynamicFormsFramework', ['ui.router'])
    
    //configuring routes for app
    .config(function($stateProvider, $urlRouterProvider) {
    
        $stateProvider
	
            // route to show our basic form (/form)
            .state('visor', {
                url: '/visor/{paramPage}',
                templateUrl: 'formTemplate.html'+'?' + new Date().getTime(),
                controller: 'VisorCtrl',
                reloadOnSearch: true,
            });
            

           
        // catch all route
        // send users to the form page 
        $urlRouterProvider.otherwise('/visor/0');
        });
    
})();

