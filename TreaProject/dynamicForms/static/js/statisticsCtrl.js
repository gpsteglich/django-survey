'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * This controller handles the logic to create, edit and save a form.
     */    
    app.controller('statisticsCtrl', function ($scope, $http, $location, $window) {
    	
    	//var stat = this;
        /*
        $http.get('/dynamicForms/statistics/'+)
                .success(function(data){
                    visor.version = data;
                    visor.pages = JSON.parse(data.json).pages;
                    visor.logic = JSON.parse(data.json).logic;
                    visor.initialiceConditions();
                    visor.changePage(0);
                })
                .error(function(data, status, headers, config){
                    alert('error loading statistics: ' + status);
                });
        */
        $scope.config = {
            title: 'Products',
            tooltips: true,
            labels: false,
            mouseover: function() {},
            mouseout: function() {},
            click: function() {},
            legend: {
                display: true,
                //could be 'left, right'
                position: 'right'
            }
        };

       $scope.data = {
            series: ['Sales', 'Income', 'Expense', 'Laptops', 'Keyboards'],
            data: [{
              x: "Laptops",
              y: [100, 500, 0],
              tooltip: "this is tooltip"
            }, {
              x: "Desktops",
              y: [300, 100, 100]
            }, {
              x: "Mobiles",
              y: [351]
            }, {
              x: "Tablets",
              y: [54, 0, 879]
            }]
          };

    });
})();