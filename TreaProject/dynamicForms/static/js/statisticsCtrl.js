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
        stat.versionNumber = ($location.search()).ver;
        stat.versionNumber = ($location.search()).ver;
        stat.versionNumber = ($location.search()).ver;
        stat.json = "";
        /*
        // $scope.templates = {
        //     'NumberField': '/dynamicForms/field_statistic/NumberField/',
        //     'SelectField': '/dynamicForms/field_statistic/SelectField/',
        //     'CheckboxField': '/dynamicForms/field_statistic/CheckboxField/',

        // }
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
        stat.filter_id='';
        stat.filter_type='';
        stat.filter_value='';
        stat.path='';
        stat.getF= function(){
        
       
          
       if(stat.filter_id!='' && stat.filter_type !='' && stat.filter_value != ''){
                stat.path = stat.filter_id +'/' +stat.filter_type +'/'+ stat.filter_value;
                console.log(stat.path);
       }else {
           stat.path='';
        }

        
        $http.get('../statistics/'+stat.formId+'/'+stat.versionNumber+'/'+stat.path)
        
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
                                'tnf': field.total_not_filled,
                                'req': field.required,
                                'type': "Number"
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
                                'tnf': field.total_not_filled,
                                'req': field.required,
                                'type': "Combobox"

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
                                'tnf': field.total_not_filled,
                                'req': field.required,
                                'type': "Checkbox"
                            }
                        }
                                        
                    }
                     console.log(stat.values);

                })
                .error(function(data, status, headers, config){
                    alert('error loading statistics: ' + data);
                });
        
        };
     
        stat.getF();
      console.log(stat.values);

      stat.Discard = function(){
        stat.filter_id='';
        stat.filter_type='';
        stat.filter_value='';
        stat.path='';
        stat.getF();



      }

       $scope.createArrayToExport  = function (field){
        var data = [];
       
            data.push({
                "Label" : "field type",
                "Value" : field.type,                               
            });
            data.push({
                "Label" : "is required",
                "Value" : field.req,                               
            });
            data.push({
                "Label" : "Answered fields",
                "Value" : field.tf,                               
            });
            data.push({
                "Label" : "Empty fields",
                "Value" : field.tnf,                               
            });
            data.push({
                "Label" : "   ",
                "Value" : '',                               
            });
        if (field.type == 'Number'){
            
            data.push({
                "Label" : "Mean",
                "Value" : field.m,                               
            });
            data.push({
                "Label" : "Total Mean",
                "Value" : field.mt,                               
            });
            data.push({
                "Label" : "Standard Deviaion",
                "Value" : field.sd,                               
            });
            data.push({
                "Label" : "Total Standard deviation",
                "Value" : field.sdt,                               
            });      
            for(var i=0; i<5; i++){
               data.push(field.data.data[i]); 
            }
        }
        else{
            // alert(data.data[1]);
            for(var i=0; i<field.data.data.length; i++){
                data.push(field.data.data[i]);
            }
        }
        return data;

    }


       $scope.createPDF = function(field){
                          
                        
                            var fontSize = 12, height = 0,doc;
                            var data = $scope.createArrayToExport(field) ;
                            doc = new jsPDF('p', 'pt', 'a4', true);
                            doc.setFont("courier", "normal");
                            doc.setFontSize(fontSize);                    
                            height = doc.drawTable(data, {xstart:10,ystart:10,tablestart:70,marginleft:50});      
                            doc.save("statistics.pdf");
                         
                           }
     

    

        
    $scope.chart_types = [
        'pie',
        'bar',
    ];    

});
})();
