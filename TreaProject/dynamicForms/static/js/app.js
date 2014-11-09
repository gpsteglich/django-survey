'use strict';

(function () {
    /*
    * Module dynamicFormsFramework  ,'angularCharts'
    * This module encapsulates the logic that will handle the form.
    */
    var app = angular.module('dynamicFormsFramework', ['ui.sortable','ui.bootstrap','checklist-model','angularCharts','ngSanitize','ngCsv'])
    .config(['$locationProvider', '$httpProvider', function ($locationProvider, $httpProvider) {

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
     

    }]);
    
})();
