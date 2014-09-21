'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * This controller handles the logic to create, edit and save a form.
     */    
    app.controller('EditorCtrl', ['$scope','$http', function ($scope, $http) {
        
    	/*
    	 * editorMode variable determines if the context is for editing or showing the
    	 * form on the fields templates. 
    	 */
    	$scope.editorMode = true;
    	
        var editor = this;
        
        editor.questions = [];

        /*
         *  'selectedField' holds the current field that is being edited.
         */
        editor.selectedField;
        
        editor.selectField = function(index) {
            editor.selectedField = editor.questions[index];
        };
        
        editor.FieldTypes = [
            'text',
            'number',
            'textarea',
            'combobox',
            'mail',
            'identityDoc'
        ];

        editor.deleteField = function(index){
            editor.questions.splice(index,1);        
        };

        editor.newField =  {
        	field_id : 0,
            field_type:'' ,
            text: '',
            required: false,
            answer: '',
        };
        
        editor.addField = function(type) {
            var newField = angular.copy(editor.newField);
            newField.field_id = editor.questions.length;
            newField.field_type = type || 'text';
            editor.questions.push(newField);
            editor.selectedField = angular.copy(editor.newField);
        };
       
        editor.clearSelectedField = function(){
            editor.selectedField = angular.copy(editor.newField);            
        };
        
        /*
         * The variable 'actualForm' defines whether the editor is creating
         * or editing a form. If it is undefined its a new form,
         * else is editing an existing one.
         */
        editor.actualForm = 1;
        editor.actualVersion = 1;
        
        if (editor.actualForm){
            /*
            * Edit Form Case
            */
                //Load Form
             $http.get('forms/'+editor.actualForm)
             .success(function(data){
                editor.form = data;
                 
                 //Load version
                $http.get('version/'+editor.actualForm+'/'+editor.actualVersion)
                .success(function(data){
                    editor.version = data;
                })
                .error(function(data, status, headers, config){
                    alert('error cargando version: ' + status);
                })
             })
             .error(function(data, status, headers, config){
                 alert('error cargando formulario: ' + status);
             })
        } else {
            /*
            * New Form Case
            */
            editor.form = {
                'title' : '',
                'slug' : '',
            };
            editor.version = {
                'status' :1 ,
                'publish_date' : '2014-06-06',
                'expiry_date' : '2014-06-06',
                'number' : 0,
                'owner' : '',
                'json' : '',
                'form' : '',
            }
        };
        
        editor.saveForm = function(){
            editor.version.status = 0;
            $http.put('forms/'+ editor.actualForm +'/', editor.form)
            .success( function(data, status, headers, config){
                editor.form.slug = data.slug;
                editor.actualForm = data.id;
                editor.version.json = JSON.stringify({'Fields' : editor.questions});
                $http.put('version/'+editor.actualForm+'/'+editor.actualVersion+'/', editor.version)
                .success( function(data, status, headers, config){
                    editor.actualVersion = data.number;
                })
                .error(function(data, status, headers, config) {
                    alert('error guardando version: ' + status);
                });
            })
            .error(function(data, status, headers, config) {
                alert('error guardando formulario: ' + status);
            });

        };
        
        /*
        editor.submitForm = function(){
        	editor.form.status = 1;
            editor.form.json = JSON.stringify({'Fields' : editor.questions});
            if (editor.actualSlug){
                $http.put('forms/'+ editor.actualSlug,editor.form)
                    .success( function(data, status, headers, config){ç
                    	
                    })
                    .error(function(data, status, headers, config) {
                    	
                    });
            } else {
                editor.form.slug = 'temp_slug';
                $http.post('forms/',editor.form)
                .success( function(data, status, headers, config){
                        editor.form.slug = data.slug;
                        editor.actualSlug = data.slug;    
                    })
                .error(function(data, status, headers, config) {
                        
                    });
            };
        };*/
        
    }]);
    
})()