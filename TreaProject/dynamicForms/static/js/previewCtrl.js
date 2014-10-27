'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * The PreviewCtrl holds the logic to display a preview of the form
     * with all its functionalities.
     */
    app.controller('PreviewCtrl', ['$scope','$http','$location','$rootScope', 'VisorService', 
            function ($scope, $http, $location, $rootScope, VisorService) {

        var preview = $scope;

        preview.urlBase = $rootScope.urlBase;

        /*
        * This controller expects as a query params the form and version to display
        */
        preview.formIdParam = ($location.search()).form;
        preview.versionIdParam = ($location.search()).ver;
        
        console.log('url params:');
        console.log('slug: '+ $location.hash().split('_')[0]);

            // Load Form
        $http.get('forms/'+preview.formIdParam)
            .success(function(data){
                preview.title = data.title;
                 //Load version
                $http.get('version/'+preview.formIdParam+'/'+preview.versionIdParam)
                .success(function(data){
                    preview.version = data;
                    preview.pages = JSON.parse(data.json).pages;
                    preview.logic = JSON.parse(data.json).logic;
                    preview.initialiceConditions();
                    preview.changePage(0);
                    preview.selectPage(0);
                })
                .error(function(data, status, headers, config){
                    alert('error loading version: ' + status);
                });
            })
            .error(function(data, status, headers, config){
                alert('error loding form: ' + status);
            });
        
        /*
        * TODO: Sería útil permitir al editor ingresar datos y que sean validados por el back
        * pero sin persistirlos en la base.
        */
        preview.save = function(){
            alert('Form was completed correctly. \nThis is a preview, the data wont be saved.');   
        };
        
        preview.selectPage = function(page){
            preview.selectedPage = preview.pages[page];
            preview.selectedPageNum = page;
        };
        
        /*
        * The page selection is fired by the change of the url
        */
        preview.changePage = function(page){
            $location.search('page',page);
        };

        /*
        * This function watches any change in the url and updates the selected page.
        */
        $scope.$on('$locationChangeSuccess', function(event) {
            var changePage = ($location.search()).page || 0;
            changePage = parseInt(changePage);
            if (changePage.isNaN){
                changePage = 0;
            }
            if (preview.pages){
                if (changePage > preview.pages.size || changePage < 0){
                    changePage = 0;   
                }
                preview.selectPage(changePage);
            }
        });









        /*
        * Page navegation
         */
        preview.canNext = function(){
            var canNext = false;
            if (preview.pages){
                canNext = (preview.selectedPageNum + 1 < preview.pages.length);
            }
            return canNext;
        };

        preview.next = function(){
            if (preview.selectedPageNum + 1 < preview.pages.length){
                preview.changePage(preview.selectedPageNum + 1);
            }
        };

        preview.canPrevious = function(){
            var canPrevious = false;
            if (preview.pages){
                canPrevious = (preview.selectedPageNum > 0);
            }
            return canPrevious;
        };

        preview.previous = function(){
            if (preview.selectedPageNum > 0){
                preview.changePage(preview.selectedPageNum - 1);
            }
        };





        preview.showValues = [];

        //Logic methods
        preview.initialiceConditions = function(){
            preview.questions = [];
            for (var i=0; i< preview.pages.length; i++) {
                preview.questions = preview.questions.concat(angular.copy(preview.pages[i].fields));
            }
            for (var j=0; j< preview.questions.length; j++){
                var field = preview.questions[j];
                preview.evaluateCondition(field.field_id);
            }
        };

        preview.updateDependencies = function(field_id){
            var field_org = preview.getFieldById(field_id);
            var field_dst;
            for (var k=0; k < field_org.dependencies.fields.length; k++){
                field_dst = preview.getFieldById(field_org.dependencies.fields[k]);
                preview.evaluateCondition(field_dst.field_id);
            }
        };

        preview.evaluateCondition = function(field_id){
            var logic = preview.logic[field_id];
                if (logic){
                    var value = true;
                    if (logic.action == 'All'){
                        value = true;
                        for (var condAll in logic.conditions){
                            var condition = logic.conditions[condAll];
                            var field_org = preview.getFieldById(condition.field);
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
                            var field_org = preview.getFieldById(condition.field);
                            var data = field_org.answer;
                            var operator = eval('operatorFactory.getOperator("'+condition.field_type+'")');
                            var funcStr = 'operator.'+ condition.comparator +'("'+data+'","'+ condition.value+'")';
                            value |= eval(funcStr);
                        }
                        
                    }
                    if (logic.operation == 'Show'){
                        preview.showValues[field_id] = value;
                    } else {
                        preview.showValues[field_id] = !value;
                    }
                } else {
                    preview.showValues[field_id] = 1;
                }
        };
        
        preview.getFieldById = function(id){
            //precondition: Field with field_id == id exists
            for(var i = 0; i < preview.pages.length; i++){
                var page = preview.pages[i];
                for(var j = 0; j < page.fields.length; j++){
                    var field = page.fields[j];
                    if(field.field_id == id){
                        return field;
                    }
                }
            }
        };

        

    }]);
})();