describe("MainPage Testing", function() {
    
    beforeEach(angular.mock.module('dynamicFormsFramework'));
    beforeEach(inject(function ($rootScope, $controller, _$location_, _$httpBackend_) {
        $location = _$location_;
        scope = $rootScope.$new();
    }));
    
    it("Testing main modes.", inject(function($controller,$rootScope) {
        var ctrl = createController();
        
        var order = [
            {name: "Id", value: "id"},
            {name: "Owner", value: "owner"},
            {name: "Title", value: "title"},
            //{name: "Publish Date", value: "publish_date"},
        ];

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