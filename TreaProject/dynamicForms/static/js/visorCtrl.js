'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework')
    
        /*
         * The VisorCtrl holds the logic to display, validate and submit the form.
         */
        .controller('VisorCtrl', ['$scope','$http','$stateParams','$state', function ($scope, $http, $stateParams, $state) {

            
            
            var visor = this;
            
            /*
             * To get the form the slug is catched form the path.
             * This should be handled by $routerprovider
             */
            //FIXME: corregir la manera de obtener el slug
            visor.slug = location.pathname.match(/\/visor\/(.*)/)[1];
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
            visor.pages = [];
            $http.get('/dynamicForms/visor/publishVersion/'+visor.slug)
                .success(function(data){
                    visor.version = data;
                    visor.pages = JSON.parse(data.json).pages;
                    //visor.selectedPage = visor.pages[0];
                    visor.selectPage($stateParams.paramPage);
                })
                .error(function(data, status, headers, config){
                    alert('error cargando las preguntas: ' + status);
                });

            visor.reload = function(page){
                //$state.go('visor',{ "paramPage": page}, { reload : true });
                visor.selectPage(page);
                //$state.reload();
                
            }
            
            visor.selectPage = function(page){
                visor.selectedPage = visor.pages[page];
            }
            
            // Parameters are only visible inside ui-view scope
            visor.routerParam = $stateParams;
            visor.param = $stateParams.paramPage;
            
            visor.save = function(){
                $http.post('/dynamicForms/visorPub/'+visor.form.slug+'/submit/',visor.questions)
                    .success( function(data, status, headers, config){

                    })
                    .error(function(data, status, headers, config) {
                        alert('Error guardando las respuestas: ' + status);
                    });
            };

        }]);
})();