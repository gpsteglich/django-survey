'use strict';

(function () {
    /*
    * Module dynamicFormsFramework
    * This module encapsulates the logic that will handle the form.
    */
    var app = angular.module('dynamicFormsFramework', ['ui.bootstrap','checklist-model', 'udpCaptcha',])
    .config(['$locationProvider','$httpProvider', function ($locationProvider, $httpProvider) {
        
        //$locationProvider.html5Mode(true);
        $locationProvider.html5Mode({
		enabled: true,
		requireBase: false
		});
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    }]);

    app.directive('validate', function() {
      return {
        require: 'ngModel',
        link: function(scope, elm, attrs, ctrl) {
          ctrl.$validators.validate = function(modelValue, viewValue) {
            if (ctrl.$isEmpty(modelValue)) {
              // consider empty models to be valid
              return true;
            }
            var validator = validatorFactory.getValidator(attrs.fieldtype);
            if (validator){
                if (validator.validate(viewValue, attrs)) {
                    // it is valid
                    return true;
                }
                // it is invalid
                return false;
            } else {
                return true;
            }
          };
        }
      };
    });


})();

