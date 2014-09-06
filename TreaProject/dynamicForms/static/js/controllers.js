'use strict';

/* Controllers */

var dynaimcFormsControllers = angular.module('dynamicFormsControllers', []);

dynaimcFormsControllers.controller('PhoneListCtrl', ['$scope', 'Phone',
  function($scope, Phone) {
    $scope.phones = Phone.query();
    $scope.orderProp = 'age';
  }]);