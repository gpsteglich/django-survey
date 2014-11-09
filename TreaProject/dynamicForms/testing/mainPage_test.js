describe("MainPage Testing", function() {
    
    beforeEach(angular.mock.module('dynamicFormsFramework'));
    beforeEach(inject(function ($rootScope, $controller, _$location_, _$httpBackend_) {
        $location = _$location_;
        scope = $rootScope.$new();
    }));
    
    it("Testing main modes.", inject(function($controller,$rootScope) {
        var ctrl = createController();
        scope.slug = 'slug';
        expect(scope.isVisorMode()).toBe(true);
        expect(scope.isPreviewMode()).toBe(false);
        scope.slug = undefined;
        scope.formIdParam = 1;
        scope.versionIdParam = 1;
        expect(scope.isVisorMode()).toBe(false);
        expect(scope.isPreviewMode()).toBe(true);
    }));

});