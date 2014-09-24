

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
        var checkboxOption = {
            label : 'new option',
        }


        
        editor.questions = [];


        /*
         *  'selectedField' holds the current field that is being edited.
         */
        editor.selectedField;
        
        editor.selectField = function(index) {
            editor.selectedField = editor.questions[index];
        };

        editor.addOption = function() {
            var option = angular.copy(checkboxOption);   
            editor.selectedField.options.push(option);
        };

        editor.deleteOption = function (index){
            editor.selectedField.options.splice(index,1);
        }
        
        editor.FieldTypes = [
            'text',
            'number',
            'textarea',
            'combobox',
            'mail',
            'identityDoc',
            'checkbox',        
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
            options: [] 
        };


        
        editor.addField = function(type) {
            var newField = angular.copy(editor.newField);
           
            if (type === editor.FieldTypes[6]){
              
                 var option1 = angular.copy(checkboxOption);
                 option1.label ='first option';
                 var option2 = angular.copy(checkboxOption);
                 option2.label ='second option';
                 var option3 = angular.copy(checkboxOption);
                 option3.label ='third option';
                newField.options= [option1,option2,option3];

            }
            newField.field_id = editor.questions.length;
            newField.field_type = type || 'text';
            editor.questions.push(newField);
            editor.selectedField = editor.questions[editor.questions.length];
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
                'status' :0 ,
                'publish_date' : '2014-06-06',
                'expiry_date' : '2014-06-06',
                'number' : 0,
                'owner' : '',
                'json' : '',
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
                    editor.questions = JSON.parse(data.json).Fields

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
                    editor.version.json = JSON.stringify({'Fields' : editor.questions});
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
                    editor.version.json = JSON.stringify({'Fields' : editor.questions});
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