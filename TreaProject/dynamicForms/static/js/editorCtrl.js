

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * This controller handles the logic to create, edit and save a form.
     */    
    app.controller('EditorCtrl', ['$scope','$http','$location', '$window', function ($scope, $http, $location, $window) {
        
    	/*
    	 * editorMode variable determines if the context is for editing or showing the
    	 * form on the fields templates. 
    	 */
    	$scope.editorMode = true;
        
        var editor = this;
        
        editor.FieldTypes = [];
        
        $http.get('constants/')
                .success(function(data){
                    editor.FieldTypes = data;
                }).error(function(status, data){
                    alert(status+' data:'+data);
                });
        
        var checkboxOption = {
            label : 'new option',
        }
        
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
        editor.getSelectedField = function(){
            if (editor.selectedField){
                return editor.selectedField.field_type || 1;
            } else {
                return 1;
            };
        };
        
        editor.selectField = function(page, index) {
            editor.selectedPage = editor.pages[page];   
            editor.selectedField = editor.selectedPage.fields[index];
        };

        editor.addOption = function() {
            var option = angular.copy(checkboxOption);   
            editor.selectedField.options.push(option);
        };

        editor.deleteOption = function (index){
            editor.selectedField.options.splice(index,1);
        }

        editor.deleteField = function(page, index){
            editor.pages[page].fields.splice(index,1);        
        };

        editor.newField =  {
        	field_id : 0,
            field_type:'' ,
            text: '',
            answer: '',
            validations: {
                required: false,
                min_number: 0,
                max_number: 100,
                max_len_text: 255,
            },
            options: ''
        };
        
        //TODO: asegurar identificador de pregunta único
        editor.addField = function(type) {
            var newField = angular.copy(editor.newField);
            newField.field_id = ++editor.max_id;
            newField.field_type = type || 1;
            if (type === editor.FieldTypes[6]){
                 var option1 = angular.copy(checkboxOption);
                 option1.label ='first option';
                 var option2 = angular.copy(checkboxOption);
                 option2.label ='second option';
                 var option3 = angular.copy(checkboxOption);
                 option3.label ='third option';
                newField.options= [option1,option2,option3];
            }
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
        
        editor.checkValidations = function(field){
            var val = field.validations;
            if (val.min_number > val.max_number) {
                alert("Minimum can't exceed maximum");
                val.min_number = val.max_number;
            };
            if (val.max_len_text < 0){
                alert("Maximum length can't be less than 0");
                val.max_len_text = 0;
            };
        };
        
        var tmpList = [];
        for (var i = 1; i <= 6; i++){
           	tmpList.push({
           		text: 'Item ' + i,
        		value: i
           	});
        }
  
        $scope.list = tmpList;
        
        /*
        * Load or create a new Form
        */
        editor.loadForm = function(){
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
                    'publish_date' : '',
                    'expiry_date' : '',
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
                        var questions = [];
                        for (var i=0; i<editor.pages.length; i++) {
                            questions = questions.concat(editor.pages[i].fields);
                        };
                        editor.max_id = Math.max.apply(Math,questions.map(function(o){
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
        };
        // Call to loadForm function on control initialization
        editor.loadForm(); 
        
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
