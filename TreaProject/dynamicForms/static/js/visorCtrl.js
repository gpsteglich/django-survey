'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework')
    
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
                })
            
                // Load Version
            $http.get('/dynamicForms/visor/publishVersion/'+visor.slug)
                .success(function(data){
                    visor.version = data;
                    visor.pages = JSON.parse(data.json).pages;
                    visor.selectPage(0);
                })
                .error(function(data, status, headers, config){
                    alert('Error loading data: ' + status);
                });

            
                // Persist form
            visor.save = function(){
             
            
            
                visor.questions = [];
                for (var i=0; i< visor.pages.length; i++) {
                    visor.questions = visor.questions.concat(angular.copy(visor.pages[i].fields));
                };
                
                
               
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

                
                
                
                
                
                for (var j=0; j< visor.questions.length; j++) {
                    delete visor.questions[j]['validations'];
                    delete visor.questions[j]['tooltip'];
                    delete visor.questions[j]['options'];
                    visor.questions[j].required = false;
                };
                
                
                
                
                
                
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
