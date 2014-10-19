'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * This controller handles the logic to create, edit and save a form.
     */    
    app.controller('statisticsCtrl', function ($scope, $http, $location, $window) {
    	
    	alert($location.absUrl());
        //alert($location.path());
        var separator = '/';
        var stat = this;
    	stat.formId = ($location.search()).form;
        stat.versionNumber = ($location.search()).ver;
        stat.json = "";
        
        stat.geeet= function(){
        
        $http.get('/dynamicForms/statistica/1/1/')
        
                .success(function(data){
                    console.log(data.mensaje);
                    stat.json = data.mensaje;
                    
                })
                .error(function(data, status, headers, config){
                    alert('error loading statistics: ' + status);
                });
        
        };
     
     stat.geeet();
      
     console.log(stat.json);
     
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