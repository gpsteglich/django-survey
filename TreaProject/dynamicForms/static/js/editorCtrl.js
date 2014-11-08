

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * This controller handles the logic to create, edit and save a form.
     */    
    app.controller('EditorCtrl', ['$scope','$http','$location', '$window', '$rootScope', 
                function ($scope, $http, $location, $window, $rootScope) {
        
    	/*
    	 * editorMode variable determines if the context is for editing or showing the
    	 * form on the fields templates. 
    	 */
        
        var editor = this;
        
        editor.urlBase = $rootScope.urlBase;

        editor.FieldTypes = [];
        
        $http.get('constants/')
                .success(function(data){
                    editor.FieldTypes = data;
                }).error(function(status, data){
                    alert(status+' data:'+data);
                });
        
        var option = {
            label : 'new option',
            id : 0
        };
        
        editor.max_id = 0;
        
        editor.newPage = {'fields':[], 'subTitle':''};
        
        editor.pages = [angular.copy(editor.newPage)];

        editor.questions = [];
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
        editor.selectedField = '';
        
        editor.getSelectedField = function(){
            if (editor.selectedField){
                return editor.selectedField.field_type || 'default';
            } else {
                return 'default';
            }
        };
        
        editor.selectField = function(page, index) {
            editor.selectedPage = editor.pages[page];   
            editor.selectedField = editor.selectedPage.fields[index];
            //select properties tab as active
            $("#myTab li:eq(1) a").tab('show');
        };

        editor.addOption = function() {
            var option1 = angular.copy(option);   
            editor.selectedField.options.push(option1);
            option1.id =  ++editor.selectedField.max_id;
        };

        editor.deleteOption = function (index){
            editor.selectedField.options.splice(index,1);
        };

        editor.deleteField = function(page, index){
             editor.questions.splice(editor.questions.indexOf(editor.pages[page].fields[index]));  
             editor.pages[page].fields.splice(index,1);  
        };
        
        editor.optionsAdded = [];
        editor.applyOptions = function(){     
            
            editor.optionsAdded = editor.optionsAdded.map(function(o){
                return { label:o.toString(), id: 0   };

            });
           
            for(var i = 0;i<editor.optionsAdded.length; i++){
                editor.optionsAdded[i].id = ++editor.selectedField.max_id;
            }            
            editor.selectedField.options = editor.selectedField.options.concat(angular.copy(editor.optionsAdded));
            editor.optionsAdded = [];
        };
    
        editor.createField = function(type){
            return fieldFactory.getField(type).buildField();
        };

        editor.addField = function(type) {
            var newField = editor.createField(type);//angular.copy(editor.newField);
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
            editor.selectedField = editor.createField(type);            
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
            if (val.min_number && val.max_number){
                if (val.min_number > val.max_number) {
                    alert("Minimum can't exceed maximum");
                    val.min_number = val.max_number;
                }
            }
            if (val.max_len_text < 0){
                alert("Maximum length can't be less than 0");
                val.max_len_text = 0;
            }
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
                };
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
                        editor.logic = JSON.parse(data.json).logic;
                        editor.after_submit = JSON.parse(data.json).after_submit;
                        editor.questions = [];
                        for (var i=0; i<editor.pages.length; i++) {
                            editor.questions = editor.questions.concat(editor.pages[i].fields);
                        }
                        editor.max_id = Math.max.apply(Math,editor.questions.map(function(o){
                            return o.field_id;
                        }));

                        if (isNaN(editor.max_id)){
                            editor.max_id = 0;
                        }
                    })
                    .error(function(data, status, headers, config){
                        alert('error cargando version: ' + status);
                    });
                })
                .error(function(data, status, headers, config){
                    alert('error cargando formulario: ' + status);
                });
            }
        };
        // Call to loadForm function on control initialization
        editor.loadForm(); 
        
        /*
        * Save and publish form
        */
        //TODO: usar variables globales para PUBLISH, DRAFT
        editor.saveForm = function(){
            if (editor.validateForm()){
                editor.persistForm(0);
            }
        };
        editor.submitForm = function(){
            if (editor.validateForm()){
                editor.persistForm(1);
            }
        };
    
        editor.validateForm = function(){
            for (var pageNum in editor.pages){
                var page = editor.pages[pageNum];
                for (var fieldIndex in page.fields){
                    var field = page.fields[fieldIndex];
                    if (field.text == null || field.text == ''){
                        f = parseInt(fieldIndex, 10) + 1;
                        p = parseInt(pageNum, 10) + 1;
                        alert ("Field labels can't be empty.");
                        return false;
                    }
                    if (field.field_type == 'SelectField' || field.field_type == 'CheckboxField'){
                        if (!field.options.length){
                            alert ("Field options can't be empty.");
                            return false;
                        }
                    }
                }
            }
            return true;
        };
        
        editor.cleanJson = function(){
            for (var fieldId in editor.logic.fields){
                var field = editor.logic.fields[fieldId];
                for (var conditionId in field.conditions){
                    var condition = field.conditions[conditionId];
                    if (condition.operatorsList){
                        //delete condition.operatorsList;
                    }
                }
            }
        };

        editor.persistForm = function(formStatus){
            editor.version.status = formStatus;
            editor.cleanJson();
            if (editor.isNewForm()){
                $http.post('forms/', editor.form)
                .success( function(data, status, headers, config){
                    editor.form = data;
                    editor.formIdParam = data.id;
                    editor.version.form = data.id;
                    editor.version.json = angular.toJson({'pages':editor.pages,'logic':editor.logic, 'after_submit':editor.after_submit});
                    $http.post('version/'+editor.formIdParam+'/', editor.version)
                    .success( function(data, status, headers, config){
                        editor.versionIdParam = data.number;
                        editor.version = data;
                        if (formStatus == 1){
                            $window.location.href = 'main';
                        } else {
                            // update the url parameters
                            $location.search({form:editor.formIdParam, ver:editor.versionIdParam});
                        }
                    })
                    .error(function(data, status, headers, config) {
                        var errors = data.error;
                        alert('error saving new version: ' + data.error);
                    });
                })
                .error(function(data, status, headers, config) {
                    alert('error saving new form: ' + data.error);
                });
            } else {
                $http.put('forms/'+ editor.formIdParam + '/', editor.form)
                .success( function(data, status, headers, config){
                    editor.form = data;
                    editor.version.json = angular.toJson({'pages':editor.pages,'logic':editor.logic,'after_submit':editor.after_submit});
                    $http.put('version/'+editor.formIdParam+'/'+editor.versionIdParam+"/", editor.version)
                    .success( function(data, status, headers, config){
                        editor.version = data;
                        if (formStatus == 1){
                            $window.location.href = 'main';
                        }
                    })
                    .error(function(data, status, headers, config) {
                        alert('error saving version: ' + data.error);
                    });
                })
                .error(function(data, status, headers, config) {
                    alert('error saving form: ' + data.error);
                });
            }

        };

        editor.getFieldById = function(id){
            //precondition: Field with field_id == id exists
            for(var i = 0; i < editor.pages.length; i++){
                var page = editor.pages[i];
                for(var j = 0; j < page.fields.length; j++){
                    var field = page.fields[j];
                    if(field.field_id == id){
                        return field;
                    }
                }
            }
        };

        editor.getPageNum = function(page){
            for (var i = 0; i < editor.pages.length; i++){
                if (editor.pages[i] == page){
                    return i;
                }
            }
        };


//------------------------------------------------LOGICA------------------------------------------------------------------------//
        // logic structures  
      
        editor.newLogicField ={
            operation : 'Show',
            action : 'All',
            conditions: [],
        };

        editor.newCondition = {
            field:'',
            comparator:'',
            value:'',
            operatorsList:[],
        };

        editor.logic = {
            fields: {},
            pages: {},
        };
        
        editor.configLogicField = function (fieldId){
            editor.questions = [];
            for (var i=0; i< editor.pages.length; i++) {
                editor.questions = editor.questions.concat(editor.pages[i].fields);
            }
            if(editor.logic.fields[fieldId]==undefined){
                editor.logicField = angular.copy(editor.newLogicField);
                
            }else{
                editor.logicField=angular.copy(editor.logic.fields[fieldId]);
                for (var cond_index in editor.logicField.conditions){
                    cond = editor.logicField.conditions[cond_index];
                    editor.selectFieldOnCondition(cond);
                }
            }
        };

        editor.configLogicPage = function (page){
            editor.questions = [];
            for (var i=0; i< editor.pages.length; i++) {
                editor.questions = editor.questions.concat(editor.pages[i].fields);
            }
            var pageNum = editor.getPageNum(page);
            if(editor.logic.pages[pageNum]==undefined){
                editor.logicField = angular.copy(editor.newLogicField);
            }else{
                editor.logicField=angular.copy(editor.logic.pages[pageNum]);
                for (var cond_index in editor.logicField.conditions){
                    cond = editor.logicField.conditions[cond_index];
                    editor.selectFieldOnCondition(cond);
                }
            }
        };

        editor.addNewLogicCondition = function (){
            var newLogicCondition = angular.copy(editor.newCondition);
            editor.logicField.conditions.push(newLogicCondition);
        };

        editor.removeLogicCondition= function(indexCond){
            editor.logicField.conditions.splice(indexCond);
        };

        editor.applyDependencies = function(fieldId){
            
            editor.logic.fields[fieldId] = angular.copy(editor.logicField);

            //clean field dependecies of every field
            for(var i = 0; i < editor.pages.length; i++){
                var page = editor.pages[i];
                for(var j = 0; j < page.fields.length; j++){
                    var field = page.fields[j];
                    field.dependencies.fields = [];
                }
            }
            //add dependencies
            for (var dest_id in editor.logic.fields){
                var dest_field = editor.logic.fields[dest_id];
                for (var k = 0; k < dest_field.conditions.length; k++){
                    origin_id = dest_field.conditions[k].field;
                    origin = editor.getFieldById(origin_id);
                    origin.dependencies.fields.push(dest_id);
                }
            }
        };

        editor.applyPageDependencies = function(page){
            pageNum = editor.getPageNum(page);
            editor.logic.pages[pageNum] = angular.copy(editor.logicField);

            //clean page dependecies of every field
            for(var i = 0; i < editor.pages.length; i++){
                var pageTemp = editor.pages[i];
                for(var j = 0; j < pageTemp.fields.length; j++){
                    var field = pageTemp.fields[j];
                    field.dependencies.pages = [];
                }
            }
  
            //add dependencies
            for (var dest_page_num in editor.logic.pages){
                var dest_page = editor.logic.pages[dest_page_num];
                for (var k = 0; k < dest_page.conditions.length; k++){
                    origin_id = dest_page.conditions[k].field;
                    origin = editor.getFieldById(origin_id);
                    origin.dependencies.pages.push(dest_page_num);
                }
            }
        };

        editor.selectFieldOnCondition = function(condition){
            condition.field_type = angular.copy(editor.getFieldType(condition.field));
            condition.operatorsList = editor.getOperatorsForField(condition.field_type);
            condition.operandKind = editor.getFieldOperandKind(condition.field_type);
            if (editor.isOptionsType(condition.operandKind)){
                var field = editor.getFieldById(condition.field);
                condition.options = field.options;
            }
            if (editor.isInputType(condition.operandKind)){
                if (condition.options){
                    delete condition.options;
                }
            }
            if (!editor.operatorsList){
                editor.operatorsList = [];
            }
        };

        editor.getFieldType = function(field_id){
            var fieldType = '';
            for (var i=0; i<editor.questions.length; i++){
                if (field_id == editor.questions[i].field_id){
                    fieldType = editor.questions[i].field_type;
                }
            }
            return fieldType;
        };

        editor.getOperatorsForField = function(field_type){
            return operatorFactory.getOperatorMethods(field_type);
        };

        editor.getFieldOperandKind = function(field_type){
            var operator = operatorFactory.getOperator(field_type);
            return operator.operandKind();
        }

        editor.isInputType = function (operandKind){
            return operandKind == 'input';
        }

        editor.isOptionsType = function (operandKind){
            return operandKind == 'options';
        }

        editor.after_submit = {
            sendMail: false,
            //mailSubject
            //mailText
            mailSender: 'santrbl@gmail.com',
            //mailRecipient
            action: 'Show Message',// can be 'Show Message' or 'Redirect To'
            message: 'Thank you. You successfully filled the form!',
            redirect: 'http://'
        }
        
    }]);
    
})();
