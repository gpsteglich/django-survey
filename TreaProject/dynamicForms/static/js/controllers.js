'use strict';

/* Controllers */

var dynaimcFormsControllers = angular.module('formListCtrl', []);

dynaimcFormsControllers.controller('PhoneListCtrl', ['$scope', 'Phone',
  function($scope, Phone) {
    $scope.phones = Phone.query();
    $scope.orderProp = 'age';
  }]);