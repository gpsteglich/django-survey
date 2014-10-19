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
            
            var separator = '_';

            /*
             * To get the form the slug is catched form the path.
             * This should be handled by $routerprovider
             */
            visor.slug = $location.hash().split(separator)[0];

            visor.selectPage = function(page){
                visor.selectedPage = visor.pages[page];
                visor.selectedPageNum = page;
            };
            
                // Load last published Version
            $http.get('/dynamicForms/visor/publishVersion/'+visor.slug)
                .success(function(data){
                    visor.version = data;
                    visor.pages = JSON.parse(data.json).pages;
                    visor.logic = JSON.parse(data.json).logic;
                    visor.initialiceConditions();
                    visor.changePage(0);
                    visor.selectPage(0);
                })
                .error(function(data, status, headers, config){
                    alert('error loading form: ' + status);
                });

            visor.showValues = [];
            visor.showPageValues = [];

            visor.initialiceConditions = function(){
                visor.questions = [];
                for (var i=0; i< visor.pages.length; i++) {
                    visor.questions = visor.questions.concat(angular.copy(visor.pages[i].fields));
                    visor.evaluatePageCondition(i);
                }
                for (var j=0; j< visor.questions.length; j++){
                    var field = visor.questions[j];
                    visor.evaluateCondition(field.field_id);
                }
                console.log(visor.showPageValues);
            };

            visor.updateDependencies = function(field_id){
                var field_org = visor.getFieldById(field_id);
                var field_dst;
                for (var k=0; k < field_org.dependencies.fields.length; k++){
                    field_dst = visor.getFieldById(field_org.dependencies.fields[k]);
                    visor.evaluateCondition(field_dst.field_id);
                }
                for (var j=0; j < field_org.dependencies.pages.length; j++){
                    visor.evaluatePageCondition(field_org.dependencies.pages[j]);
                }
                console.log(visor.showPageValues);
            };

            visor.evaluateCondition = function(field_id){
                var logic = visor.logic.fields[field_id];
                if (logic){
                    var value = true;
                    if (logic.action == 'All'){
                        value = true;
                        for (var condAll in logic.conditions){
                            var condition = logic.conditions[condAll];
                            var field_org = visor.getFieldById(condition.field);
                            var data = field_org.answer; 
                            var operator = eval('operatorFactory.getOperator("'+condition.field_type+'")');
                            var funcStr = 'operator.'+ condition.comparator +'("'+data+'","'+ condition.value+'")';
                            value &= eval(funcStr);
                        }
                        
                    }
                    if (logic.action == 'Any'){
                        value = false;
                        for (var condAny in logic.conditions){
                            var condition = logic.conditions[condAny];
                            var field_org = visor.getFieldById(condition.field);
                            var data = field_org.answer;
                            var operator = eval('operatorFactory.getOperator("'+condition.field_type+'")');
                            var funcStr = 'operator.'+ condition.comparator +'("'+data+'","'+ condition.value+'")';
                            value |= eval(funcStr);
                        }
                        
                    }
                    if (logic.operation == 'Show'){
                        visor.showValues[field_id] = value;
                    } else {
                        visor.showValues[field_id] = !value;
                    }
                } else {
                    visor.showValues[field_id] = 1;
                }
            };

            visor.evaluatePageCondition = function(pageNum){
                var logic = visor.logic.pages[pageNum];
                if (logic){
                    var value = true;
                    if (logic.action == 'All'){
                        value = true;
                        for (var condAll in logic.conditions){
                            var condition = logic.conditions[condAll];
                            var field_org = visor.getFieldById(condition.field);
                            var data = field_org.answer; 
                            var operator = eval('operatorFactory.getOperator("'+condition.field_type+'")');
                            var funcStr = 'operator.'+ condition.comparator +'("'+data+'","'+ condition.value+'")';
                            value &= eval(funcStr);
                        }
                        
                    }
                    if (logic.action == 'Any'){
                        value = false;
                        for (var condAny in logic.conditions){
                            var condition = logic.conditions[condAny];
                            var field_org = visor.getFieldById(condition.field);
                            var data = field_org.answer;
                            var operator = eval('operatorFactory.getOperator("'+condition.field_type+'")');
                            var funcStr = 'operator.'+ condition.comparator +'("'+data+'","'+ condition.value+'")';
                            value |= eval(funcStr);
                        }
                        
                    }
                    if (logic.operation == 'Show'){
                        visor.showPageValues[pageNum] = value;
                    } else {
                        visor.showPageValues[pageNum] = !value;
                    }
                } else {
                    visor.showPageValues[pageNum] = 1;
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
                         //alert("question " + i + " options:  " + visor.questions[i].options); //take out when finished
                    }else{
                        visor.questions[i].options= visor.questions[i].options.join('#');
                         //alert("question " + i + " options:  " + visor.questions[i].options); //take out when finished
                    }
                    visor.questions[i].answer = visor.questions[i].answer.join('#');
                    //alert('question ' + i + ' answer: ' + visor.questions[i].answer); //take out when finished

                }
                //FIXME: Ver si se puede emprolijar o es la única solución
                for (var j=0; j< visor.questions.length; j++) {
                    visor.questions[j].required = visor.questions[j].validations['required'];
                    delete visor.questions[j].validations;
                    delete visor.questions[j].tooltip;
                    delete visor.questions[j].options;
                    delete visor.questions[j].dependencies;
                };
                $http.post('/dynamicForms/visor/submit/'+visor.slug,visor.questions)
                    .success( function(data, status, headers, config){
                        $window.location.href = '/dynamicForms/visor/form/submitted';
                        //alert('The data was saved correctly');
                    })
                    .error(function(data, status, headers, config) {
                        alert('Error saving data: ' + data.error);
                    });
            };
            
            /*
            * The page selection is fired by the change of the url
            */
            visor.changePage = function(page){
                $location.hash(visor.slug + separator + page);
            };
            
            /*
            * This function watches any change in the url and updates the selected page.
            */
            visor.$on('$locationChangeSuccess', function(event) {
                var hash = $location.hash();
                var changePage = $location.hash().split(separator)[1] || 0;
                changePage = parseInt(changePage);
                if (changePage.isNaN){
                    changePage = 0;
                }
                if (visor.pages){
                    if (changePage > visor.pages.size){
                        changePage = 0;   
                    }
                    visor.selectPage(changePage);
                }
            });

            /*
            * Page navegation
             */

            visor.getNext = function(){
                var next = visor.selectedPageNum + 1;
                while (next < visor.pages.length && !visor.showPageValues[next]){
                    next++;
                }
                if (next == visor.pages.length){
                    return -1;
                } else {
                    return next;
                }
            }

            visor.getPrevious = function(){
                var prev = visor.selectedPageNum - 1;
                while (prev >= 0 && !visor.showPageValues[prev]){
                    prev--;
                }
                return prev;
            }
           
            visor.canNext = function(){
                var canNext = false;
                if (visor.pages){
                    var next = visor.getNext();
                    canNext = (next != -1);
                }
                return canNext;
            };

            visor.next = function(){
                var next = visor.getNext();
                if (next != -1){
                    visor.changePage(next);
                }
            };

            visor.canPrevious = function(){
                var canPrevious = false;
                if (visor.pages){
                    var prev = visor.getPrevious();
                    canPrevious = (prev != -1);
                }
                return canPrevious;
            };

            visor.previous = function(){
                var prev = visor.getPrevious();
                if (prev != -1){
                    visor.changePage(prev);
                }
            };

        }]);
})();
