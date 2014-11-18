'use strict';

(function () {
    /*
    * Module dynamicFormsFramework
    * This module encapsulates the logic that will handle the form.
    */
    angular.module('dynamicFormsFrameworkAdmin', ['ui.sortable','ui.bootstrap','checklist-model','angularCharts'])
    .config(['$locationProvider', '$httpProvider', function ($locationProvider, $httpProvider) {

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
     
    }]);
    
})();
