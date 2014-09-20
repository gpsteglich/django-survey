'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * The VisorCtrl holds the logic to display, validate and submit the form.
     */
    app.controller('VisorCtrl', ['$scope','$http', function ($scope, $http) {

        var visor = this;
        
        /*
         * To get the form the slug is catched form the path.
         * This should be handled by $routerprovider
         */
        //FIXME: corregir la manera de obtener el slug
        visor.slug = location.pathname.match(/\/visor\/(.*)/)[1];
        visor.versionNum = 1;
        visor.title = '';
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
             visor.questions = JSON.parse(data.json).Fields;
         })
         .error(function(data, status, headers, config){
             alert('error cargando las preguntas: ' + status);
         })
    }]);
})();