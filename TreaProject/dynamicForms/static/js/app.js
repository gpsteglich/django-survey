'use strict';

(function () {
    /*
    * Module dynamicFormsFramework
    * This module encapsulates the logic that will handle the form.
    */
    var app = angular.module('dynamicFormsFramework', ['ui.sortable','ui.bootstrap'])
    .config(['$locationProvider', function ($locationProvider) {
        //$locationProvider.html5Mode(true).hashPrefix('!');
    }]);
    
})();

