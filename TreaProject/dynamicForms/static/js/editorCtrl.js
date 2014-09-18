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
            'textarea'            
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
         * The variable 'actualSlug' defines whether the editor is creating
         * or editing a form. If it is undefined its a new form,
         * else is editing an existing one.
         */
        editor.actualSlug;
        
        if (editor.actualSlug){
             $http.get('forms/'+editor.actualSlug).success(function(data){
                editor.form = data;
                editor.actualSlug = data.slug;
                var jsonStr = data.json;            
                editor.jsonStr = jsonStr;
                editor.questions = JSON.parse(jsonStr).Fields;

            });
        } else {
            editor.form = {
                'title' : '',
                'slug' : '',
                'status' : 1,
                'publish_date' : '2014-06-06',
                'expiry_date' : '2014-06-06',
                'version' : 0,
                'owner' : '',
                'json' : ''
            };
        };
        
        editor.submitForm = function(){
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
        };
        
    }]);
    
})()