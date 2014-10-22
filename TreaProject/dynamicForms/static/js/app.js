'use strict';

var url = '/dyn/';

(function () {
    /*
    * Module dynamicFormsFramework
    * This module encapsulates the logic that will handle the form.
    */
    var app = angular.module('dynamicFormsFramework', ['ui.sortable','ui.bootstrap','checklist-model'])
    .config(['$locationProvider', '$httpProvider', function ($locationProvider, $httpProvider) {

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    }]).run(function($rootScope) {
      	$rootScope.urlBase = url;
    });
})();
