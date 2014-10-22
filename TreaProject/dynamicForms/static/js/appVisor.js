'use strict';

var url = '/dyn/';

(function () {
    /*
    * Module dynamicFormsFramework
    * This module encapsulates the logic that will handle the form.
    */
    var app = angular.module('dynamicFormsFramework', ['ui.bootstrap','checklist-model'])
    .config(['$locationProvider','$httpProvider', function ($locationProvider, $httpProvider) {
        
        //$locationProvider.html5Mode(true);
        $locationProvider.html5Mode({
		enabled: true,
		requireBase: false
		});
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    }]).run(function($rootScope) {
      	$rootScope.urlBase = url;
    });

})();

