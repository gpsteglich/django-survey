'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * This controller handles the logic to create, edit and save a form.
     */    
    app.controller('statisticsCtrl', function ($scope, $http, $location, $window) {
    	
    	var stat = this;
        
        stat.mensaje = "se comunican";
        
        alert('entro al controlador');
        
        stat.config = {
                  title: '',
                  tooltips: true,
                  labels: false,
                  mouseover: function() {},
                  mouseout: function() {},
                  click: function() {},
                  legend: {
                    display: true,
                    //could be 'left, right'
                    position: 'left'
                  },
                  innerRadius: 0, // applicable on pieCharts, can be a percentage like '50%'
                  lineLegend: 'lineEnd' // can be also 'traditional'
                    }
        
        stat.data = {
                  "series": [
                    "Sales",
                    "Income",
                    "Expense"
                  ],
                  "data": [
                    {
                      "x": "Computers",
                      "y": [
                        54,
                        0,
                        879
                      ],
                      "tooltip": "This is a tooltip"
                    }
                  ]
                }
        /*
        
        mainPage.formSlugParam = ($location.search()).form;
        mainPage.versionIdParam = ($location.search()).ver;
        mainPage.orders = [
            {name: "Id", value: "id"},
            {name: "Owner", value: "owner"},
            {name: "Title", value: "title"},
            //{name: "Publish Date", value: "publish_date"},
        ]

        mainPage.selectascdsc = function(ascdsc){
            mainPage.ascdsc = ascdsc;
        }

        mainPage.url = function(){
            var parser = $location.absUrl();
            var arr = parser.split('/');
            var crit = arr[arr.length - 3];
            var sent = arr[arr.length - 2];
            return ([crit, sent]);
        }

     
    
        mainPage.getResponses = function(){
            $http.get('/dynamicForms/responses/'+mainPage.formSlugParam+'/'+ mainPage.versionIdParam+'/')
            .success(function(data){
                mainPage.json = data;
            })
            .error(function(data, status, headers, config){
                alert('Error loading form data: ' + status);
            })
        }
        */
        
    }]);
})();