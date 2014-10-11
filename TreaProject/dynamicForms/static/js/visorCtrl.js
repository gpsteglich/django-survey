'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
        /*
         * The VisorCtrl holds the logic to display, validate and submit the form.
         */
        app.controller('VisorCtrl', ['$scope','$http','$location', '$window', function ($scope, $http, $location, $window) {

            /*
            *  This controller is initialiced by ui-router, so it cant be used with ng-controller
            *  It uses $scope to make variables available for the page.
            */
            var visor = $scope;
       
            /*
             * To get the form the slug is catched form the path.
             * This should be handled by $routerprovider
             */
            //FIXME: corregir la manera de obtener el slug
            visor.slug = $location.absUrl().match(/\/visor\/([^/]*)/)[1];
            
            visor.selectPage = function(page){
                visor.selectedPage = visor.pages[page];
            }
            
                // Load Form
            $http.get('/dynamicForms/form/'+visor.slug)
                .success(function(data){
                    visor.title = data.title;
                    visor.form = data;
                })
                .error(function(data, status, headers, config){
                    alert('Error loading form: ' + status);
                });
            
                // Load Version
            $http.get('/dynamicForms/visor/publishVersion/'+visor.slug)
                .success(function(data){
                    visor.version = data;
                    visor.pages = JSON.parse(data.json).pages;
                    visor.logic = JSON.parse(data.json).logic;
                    visor.initialiceConditions();
                    visor.selectPage(0);
                })
                .error(function(data, status, headers, config){
                    alert('Error loading data: ' + status);
                });

            visor.hideValues = [];
            visor.showValues = [];

            visor.initialiceConditions = function(){
                visor.questions = [];
                for (var i=0; i< visor.pages.length; i++) {
                    visor.questions = visor.questions.concat(angular.copy(visor.pages[i].fields));
                }
                for (var j=0; j< visor.questions.length; j++){
                    var field = visor.questions[j];
                    visor.evaluateCondition(field.field_id, '');
                }
            };

            visor.updateDependencies = function(field_id){
                var field = visor.getFieldById(field_id);
                for (var k=0; k < field.dependencies.fields.length; k++){
                    visor.evaluateCondition(field.dependencies.fields[k],field.answer);
                }
            };

            visor.evaluateCondition = function(field_id, data){
                var logic = visor.logic[field_id];
                    if (logic){
                        var value = true;
                        if (logic.action == 'All'){
                            value = true;
                            for (var condAll in logic.conditions){
                                var condition = logic.conditions[condAll];
                                var operator = eval('operatorFactory.getOperator("'+condition.field_type+'")');
                                var funcStr = 'operator.'+ condition.comparator +'("'+data+'","'+ condition.value+'")';
                                value &= eval(funcStr);
                            }
                            
                        }
                        if (logic.action == 'Any'){
                            value = false;
                            for (var condAny in logic.conditions){
                                var condition = logic.conditions[condAny];
                                var operator = eval('operatorFactory.getOperator("'+condition.field_type+'")');
                                var funcStr = 'operator.'+ condition.comparator +'("'+data+'","'+ condition.value+'")';
                                value |= eval(funcStr);
                            }
                            
                        }
                        if (logic.operation == 'Show'){
                            visor.hideValues[field_id] = 0;
                            visor.showValues[field_id] = value;
                        } else {
                            visor.hideValues[field_id] = value;
                            visor.showValues[field_id] = 0;
                        }
                    } else {
                        visor.hideValues[field_id] = 0;
                        visor.showValues[field_id] = 1;
                    }
            };
            
            visor.getFieldById = function(id){
                //precondition: Field with field_id == id exists
                for(var i = 0; i < visor.pages.length; i++){
                    var page = visor.pages[i];
                    for(var j = 0; j < page.fields.length; j++){
                        var field = page.fields[j];
                        if(field.field_id == id){
                            return field;
                        }
                    }
                }
            };

                // Persist form
            visor.save = function(){
                visor.questions = [];
                for (var i=0; i< visor.pages.length; i++) {
                    visor.questions = visor.questions.concat(angular.copy(visor.pages[i].fields));
                }
                
                for ( var i = 0; i < visor.questions.length; i++) { 
                    if (visor.questions[i].field_type == 'checkbox'){
                        var respuesta = '';
                         for ( var x = 0; x < visor.questions[i].options.length-1; x++){
                            respuesta += visor.questions[i].options[x].label + '#';
                         }
                        respuesta += visor.questions[i].options[visor.questions[i].options.length-1].label;
                        visor.questions[i].options = respuesta;
                         alert("question " + i + " options:  " + visor.questions[i].options); //take out when finished
                    }else{
                        visor.questions[i].options= visor.questions[i].options.join('#');
                         alert("question " + i + " options:  " + visor.questions[i].options); //take out when finished
                    }
                    visor.questions[i].answer = visor.questions[i].answer.join('#');
                    alert('question ' + i + ' answer: ' + visor.questions[i].answer); //take out when finished

                }
                //FIXME: Ver si se puede emprolijar o es la única solución
                for (var j=0; j< visor.questions.length; j++) {
                    delete visor.questions[j].validations;
                    delete visor.questions[j].tooltip;
                    delete visor.questions[j].options;
                    visor.questions[j].required = false;
                }

                $http.post('/dynamicForms/visorPub/'+visor.form.slug+'/submit/',visor.questions)
                    .success( function(data, status, headers, config){
                       
                        $window.location.href = '/dynamicForms/visor/form/submitted';

                    })
                    .error(function(data, status, headers, config) {
                        alert('Error saving data: ' + status);
                    });
            };
            
            /*
            * The page selection is fired by the change of the url
            */
            visor.changePage = function(page){
                $location.hash(page);
            };
            
            /*
            * This function watches any change in the url and updates the selected page.
            */
            $scope.$on('$locationChangeSuccess', function(event) {
                var changePage = $location.hash() || 0;
                if (visor.pages){
                    if (changePage > visor.pages.size){
                        changePage = 0;   
                    }
                    visor.selectPage(changePage);
                }
            });

            var ob = eval('operatorFactory.getOperator("number")');
            console.log(eval('ob.greater_than("8","3")'));
        }]);
})();
