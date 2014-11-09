describe("MainPage Testing", function() {
    
    beforeEach(angular.mock.module('dynamicFormsFrameworkAdmin'));
    beforeEach(inject(function ($rootScope, $controller, _$location_, _$httpBackend_) {
        $location = _$location_;
        scope = $rootScope.$new();
        createController = function() {
            return $controller('MainPageCtrl', {
                '$scope': scope
            });
        };
    }));
    
    it("Testing main modes.", inject(function($controller,$rootScope) {
        var ctrl = createController();
        
        var order = [
            {name: "Id", value: "id"},
            {name: "Owner", value: "owner"},
            {name: "Title", value: "title"},
        ];
        console.log('orders '+order.toSource());
        console.log('ctrl.orders '+ctrl.orders.toSource());
        console.log(order == ctrl.orders);
        order = angular.copy(ctrl.orders);
        expect(ctrl.orders).toBe(order);
        /*
        expect(scope.isPreviewMode()).toBe(false);
        scope.slug = undefined;
        scope.formIdParam = 1;
        scope.versionIdParam = 1;
        expect(scope.isVisorMode()).toBe(false);
        expect(scope.isPreviewMode()).toBe(true);*/
    }));

});