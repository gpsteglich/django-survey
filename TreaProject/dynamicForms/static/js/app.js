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
	
            // state to show form in visor
            .state('visor', {
                url: '/visor/{paramPage}',
                templateUrl: 'formTemplate.html',
                controller: 'VisorCtrl',
            });
            
        // catch all route
        // send users to the form's first page 
        $urlRouterProvider.otherwise('/visor/0');
        });
    
})();

