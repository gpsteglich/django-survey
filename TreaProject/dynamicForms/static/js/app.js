'use strict';

(function () {
    /*
    * Module dynamicFormsFramework
    * This module encapsulates the logic that will handle the form.
    */
    var app = angular.module('dynamicFormsFramework', ['ui.router'])
        .config(function($stateProvider, $urlRouterProvider) {
    
            $stateProvider
	
            // route to show our basic form (/form)
            .state('visor', {
                url: '/dynamicForms/visor/:formSlug/',
                //templateUrl: 'form.html',
                //controller: 'formController'
                controller: function($scope, $stateParams) {
                    // get the id
                    $scope.formSlug = $stateParams.formSlug;
                }
            });

            // nested states 
            // each of these sections will have their own view
            // url will be nested (/form/profile)
            /*.state('form.profile', {
                url: '/profile',
                templateUrl: 'form-profile.html'
            })

            // url will be /form/interests
            .state('form.interests', {
                url: '/interests',
                templateUrl: 'form-interests.html'
            })

            // url will be /form/payment
            .state('form.payment', {
                url: '/payment',
                templateUrl: 'form-payment.html'
            });*/
        });
    
})();

