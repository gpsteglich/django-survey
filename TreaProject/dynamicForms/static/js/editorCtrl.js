

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * This controller handles the logic to create, edit and save a form.
     */    
    app.controller('EditorCtrl', ['$scope','$http','$location', function ($scope, $http, $location) {
        
    	/*
    	 * editorMode variable determines if the context is for editing or showing the
    	 * form on the fields templates. 
    	 */
    	$scope.editorMode = true;
        
        var editor = this;
        
        editor.max_id = 0;
        
        editor.newPage = {'fields':[], 'subTitle':''};
        
        editor.pages = [angular.copy(editor.newPage)];
        //editor.questions = [];
        //editor.pages[0].fields = editor.questions;

        /*
        * 'selectedPage' holds the current page that's being edited
        */
        editor.selectedPage = editor.pages[0];
        
        editor.selectPage = function(index) {
            editor.selectedPage = editor.pages[index];   
        };
        editor.addPage = function() {
            newPage = angular.copy(editor.newPage);
            editor.pages.push(newPage);   
        };
        editor.deletePage = function(index){
            //TODO: Add modal asking confirmation..
            editor.pages.splice(index,1);
            
        };
        
        /*
         *  'selectedField' holds the current field that is being edited.
         */
        editor.selectedField;
        
        editor.selectField = function(page, index) {
            editor.selectedPage = editor.pages[page];   
            editor.selectedField = editor.selectedPage.fields[index];
        };
        
        editor.FieldTypes = [
            'text',
            'number',
            'textarea',
            'combobox',
            'mail',
            'identityDoc'
        ];

        editor.deleteField = function(page, index){
            editor.pages[page].fields.splice(index,1);        
        };

        editor.newField =  {
        	field_id : 0,
            field_type:'' ,
            text: '',
            required: false,
            answer: '',
        };
        
        //TODO: asegurar identificador de pregunta único
        editor.addField = function(type) {
            var newField = angular.copy(editor.newField);
            newField.field_id = ++editor.max_id;
            newField.field_type = type || 'text';
            editor.selectedPage.fields.push(newField);
            editor.selectedField = editor.selectedPage.fields[editor.selectedPage.fields.length];
        };
       
        editor.clearSelectedField = function(){
            editor.selectedField = angular.copy(editor.newField);            
        };
        
        /*
        * This controller expects a query params to edit an existing form's version (e.g. path#?form=1&ver=1),
        * if the param is empty then it creats a new form.
        */
        editor.formIdParam = ($location.search()).form;
        editor.versionIdParam = ($location.search()).ver;
    
        editor.isNewForm = function(){
            return !(Boolean(editor.formIdParam) && Boolean(editor.versionIdParam));
        };
        
        
        /*
        * Load or create a new Form
        */
        if (editor.isNewForm()){
            /*
            * New Form Case
            */
            editor.form = {
                'title' : '',
                'slug' : '',
            };
            editor.version = {
                'json' : '',
                'status' :0 ,
                'publish_date' : '2014-06-06',
                'expiry_date' : '2014-06-06',
                'number' : 0,
                'owner' : '',
                'form' : '',
            }
        } else {
            /*
            * Edit Form Case
            */
                //Load Form
            $http.get('forms/'+editor.formIdParam)
            .success(function(data){
                editor.form = data;
                 
                 //Load version
                $http.get('version/'+editor.formIdParam+'/'+editor.versionIdParam)
                .success(function(data){
                    editor.version = data;
                    editor.pages = JSON.parse(data.json).pages;
                    editor.questions = [];
                    for (var i=0; i<editor.pages.length; i++) {
                        editor.questions = editor.questions.concat(editor.pages[i].fields);
                    };
                    editor.max_id = Math.max.apply(Math,editor.questions.map(function(o){
                        return o.field_id;
                    }));
                })
                .error(function(data, status, headers, config){
                    alert('error cargando version: ' + status);
                })
            })
            .error(function(data, status, headers, config){
                alert('error cargando formulario: ' + status);
            })
        };
        
        /*
        * Save and publish form
        */
        //TODO: usar variables globales para PUBLISH, DRAFT
        editor.saveForm = function(){
            editor.persistForm(0);
        }
        editor.submitForm = function(){
            editor.persistForm(1);
        }
        
        editor.persistForm = function(status){
            editor.version.status = status;
            if (editor.isNewForm()){
                $http.post('forms/', editor.form)
                .success( function(data, status, headers, config){
                    editor.form = data;
                    editor.formIdParam = data.id;
                    editor.version.form = data.id;
                    editor.version.json = angular.toJson({'pages':editor.pages});
                    $http.post('version/'+editor.formIdParam+'/', editor.version)
                    .success( function(data, status, headers, config){
                        editor.versionIdParam = data.number;
                        editor.version = data;
                        // update the url parameters
                        $location.search({form:editor.formIdParam, ver:editor.versionIdParam});
                    })
                    .error(function(data, status, headers, config) {
                        var errors = data.error;
                        alert('error saving new version: ' + status);
                    });
                })
                .error(function(data, status, headers, config) {
                    alert('error saving new form: ' + status);
                });
            } else {
                $http.put('forms/'+ editor.formIdParam + '/', editor.form)
                .success( function(data, status, headers, config){
                    editor.form = data;
                    editor.version.json = angular.toJson({'pages':editor.pages});
                    $http.put('version/'+editor.formIdParam+'/'+editor.versionIdParam+"/", editor.version)
                    .success( function(data, status, headers, config){
                        editor.version = data;
                    })
                    .error(function(data, status, headers, config) {
                        alert('error saving version: ' + status);
                    });
                })
                .error(function(data, status, headers, config) {
                    alert('error saving form: ' + status);
                });
            }

        };
        
    }]);
    
})()