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
        visor.path = location.pathname.match(/\/visor\/(.*)/)[1];
        visor.versionNum = 1;
            //Load Form
        $http.get('/dynamicForms/visor/publishVersion/'+visor.path)
         .success(function(data){
            visor.version = data;
             visor.questions = JSON.parse(data.json).Fields;
            /*    //Load version
            $http.get('version/'+visor.path+'/'+visor.versionNum)
            .success(function(data){
                visor.version = data;
                visor.questions = JSON.parse(data.json).Fields;
            })
            .error(function(data, status, headers, config){
                alert('error cargando version: ' + status);
            })*/
         })
         .error(function(data, status, headers, config){
             alert('error cargando formulario: ' + status);
         })
    }]);
})();