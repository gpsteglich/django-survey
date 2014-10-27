'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * This controller handles the logic to create, edit and save a form.
     */    
    app.controller('statisticsCtrl', function ($scope, $http, $location, $window, $filter) {
    	
        var separator = '/';
        var stat = this;
    	stat.formId = ($location.search()).form;
        stat.versionNumber = ($location.search()).ver;
        stat.json = "";
        /*
        $scope.templates = {
            'NumberField': '/dynamicForms/field_statistic/NumberField/',
            'SelectField': '/dynamicForms/field_statistic/SelectField/',
            'CheckboxField': '/dynamicForms/field_statistic/CheckboxField/',

        }*/
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
                position: 'right'
            }
        };

        stat.data = {
            series: [],
            data: [{
              x: "",
              y: []
            }]
          };
        
        stat.values ={
        };
        
        stat.getF= function(){
        
        $http.get('/dynamicForms/statistics/'+stat.formId+'/'+stat.versionNumber+'/')
        
                .success(function(data){
                    stat.json = JSON.parse(JSON.stringify(data));
                    console.log(stat.json);
                    for(var field_id in stat.json){
                        var field = $.extend({}, stat.json[field_id]);
                        if (field.field_type=='NumberField'){
                            var conf = angular.copy(stat.config);
                            conf.title = field.field_text;
                            var d = angular.copy(stat.data);
                            for(var i=0; i<5; i++){
                                d.data[i] = {
                                    'x': field.quintilesX[i],
                                    'y': [field.quintilesY[i]]
                                }
                            }
                            stat.values[field_id] = {
                                'id': field_id,
                                'chart': 'pie',
                                'field_type': 'NumberField',  
                                'conf': conf,
                                'data': d,
                                'm' : field.mean,
                                'mt' : field.total_mean,
                                'sd' : field.standard_deviation,
                                'sdt' : field.total_standard_deviation,
                                'tf' : field.total_filled,
                                'tnf': field.total_not_filled
                            }
                        } else if (field.field_type=='SelectField'){
                            var conf = angular.copy(stat.config);
                            conf.title = field.field_text;
                            var d = angular.copy(stat.data);
                            for(var i=0; i<field.total_per_option.length; i++){
                                d.data[i] = {
                                    'x': field.options[i],
                                    'y': [field.total_per_option[i]]
                                }
                            }
                            stat.values[field_id] = {
                                'id': field_id,
                                'chart': 'pie',
                                'field_type': 'SelectField',  
                                'conf': conf,
                                'data': d,
                                'tf' : field.total_filled,
                                'tnf': field.total_not_filled
                            }
                        } else if (field.field_type=='CheckboxField'){
                            var conf = angular.copy(stat.config);
                            conf.title = field.field_text;
                            var d = angular.copy(stat.data);
                            for(var i=0; i<field.total_per_option.length; i++){
                                d.data[i] = {
                                    'x': field.options[i],
                                    'y': [field.total_per_option[i]]
                                }
                            }
                            stat.values[field_id] = {
                                'id': field_id,
                                'chart': 'pie',
                                'field_type': 'CheckboxField',  
                                'conf': conf,
                                'data': d,
                                'tf' : field.total_filled,
                                'tnf': field.total_not_filled
                            }
                        }
                                        
                    }
                     console.log(stat.values);

                })
                .error(function(data, status, headers, config){
                    alert('error loading statistics: ' + status);
                });
        
        };
     
        stat.getF();
      console.log(stat.values);
        
    $scope.chart_types = [
        'pie',
        'bar',
    ];    

});
})();
