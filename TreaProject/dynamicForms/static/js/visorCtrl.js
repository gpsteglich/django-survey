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
            visor.slug = location.pathname.match(/\/visor\/(.*)/)[1];
            
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
                    alert('error cargando formulario: ' + status);
                })
            
                // Load Version
            $http.get('/dynamicForms/visor/publishVersion/'+visor.slug)
                .success(function(data){
                    visor.version = data;
                    visor.pages = JSON.parse(data.json).pages;
                    visor.selectPage(0);
                })
                .error(function(data, status, headers, config){
                    alert('error cargando las preguntas: ' + status);
                });

            
                // Persist form
            visor.save = function(){
                visor.questions = [];
                for (var i=0; i< visor.pages.length; i++) {
                    visor.questions = visor.questions.concat(angular.copy(visor.pages[i].fields));
                };
                for (var j=0; j< visor.questions.length; j++) {
                    delete visor.questions[j]['validations'];
                    visor.questions[j].required = false;
                };
                $http.post('/dynamicForms/visorPub/'+visor.form.slug+'/submit/',visor.questions)
                    .success( function(data, status, headers, config){

                    })
                    .error(function(data, status, headers, config) {
                        alert('Error guardando las respuestas: ' + status);
                    });
            };
            
            visor.changePage = function(page){
                $location.path('/'+ page);
            }
            
            /*
            * 
            */
            /*
            $scope.$on('$locationChangeSuccess', function(event) {
                var changePage = parseInt(($location.search()).pag) || 0;
                if (visor.pages){
                    visor.selectPage(changePage);
                }
            });*/

        }]);
})();