'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework')
    
        /*
         * The VisorCtrl holds the logic to display, validate and submit the form.
         */
        .controller('VisorCtrl', ['$scope','$http','$location', function ($scope, $http, $location) {

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
            
                // Load last published Version
            $http.get('/dynamicForms/visor/publishVersion/'+visor.slug)
                .success(function(data){
                    visor.version = data;
                    visor.pages = JSON.parse(data.json).pages;
                    visor.selectPage(0);
                })
                .error(function(data, status, headers, config){
                    alert('error loading form: ' + status);
                });

            
                // Persist form
            visor.save = function(){
                visor.questions = [];
                for (var i=0; i< visor.pages.length; i++) {
                    visor.questions = visor.questions.concat(angular.copy(visor.pages[i].fields));
                };
                for (var j=0; j< visor.questions.length; j++) {
                    delete visor.questions[j]['validations'];
                    delete visor.questions[j]['options'];
                    visor.questions[j].required = false;
                };
                $http.post('/dynamicForms/visor/submit/'+visor.slug,visor.questions)
                    .success( function(data, status, headers, config){
                        alert('The data was saved correctly');
                    })
                    .error(function(data, status, headers, config) {
                        alert('Error saving the form: ' + status + '\n data: ' + data)
                    });
            };
            
            /*
            * The page selection is fired by the change of the url
            */
            visor.changePage = function(page){
                $location.hash(page);
            }
            
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

        }]);
})();