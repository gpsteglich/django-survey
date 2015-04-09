var app = angular.module('dynamicFormsFrameworkAdmin');

app.factory('ConstantService', function($resource){
    var constants_api_url = '/dynamicForms/constants/'

    return $resource( constants_api_url, {},
        {'query': {method: 'GET', isArray: true }});
});

app.factory('FieldEditService', function($resource){
    var field_edit_api_url = '/dynamicForms/field_edit/'

    return $resource( field_edit_api_url + ':field/', {},
        {'query': {method: 'GET', isArray: true }});
});

app.factory('FormService', function($resource){
    var form_api_url = '/dynamicForms/forms/'

    return $resource( form_api_url + ':id/', {},
        {'query': {method: 'GET', isArray: true },
        'create': {method: 'POST'},
        'update': {method: 'PUT'}});
});

app.factory('VersionService', function($resource){
    var version_api_url = '/dynamicForms/version/'

    return $resource( version_api_url + ':formId/'+ ':versionId/', 
        {formId: '@formId', versionId:'@versionId'},
        {'query': {method: 'GET', isArray: true },
        'create': {method: 'POST'},
        'update': {method: 'PUT'}});
});


app.factory('ResponsesService', function($resource){
    var responses_api_url = '/dynamicForms/responses/'

    return $resource( responses_api_url + ':formId/'+ ':versionId/',
        {formId: '@formId', versionId:'@versionId'},
        {'query': {method: 'GET', isArray: true}});
});

app.factory('StatisticsService', function($resource){
    var statistics_api_url = '/dynamicForms/statistics/'

    return $resource( statistics_api_url + ':formId/'+ ':versionId/',
        {formId: '@formId', versionId:'@versionId'},
        {'query': {method: 'GET', isArray: true}});
});