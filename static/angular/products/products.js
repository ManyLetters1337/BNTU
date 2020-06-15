angular.module('angularApp.products', [
    'products.product',
    'constansApiUrls'
])

.config(function config($stateProvider) {
    $stateProvider
        .state('productInformation', {
            url: '/products/:uuid',
            params: { uuid : null },
            controller: 'ProductController',
            templateUrl: 'static/angular/products/templates/product.html'
        })

})

.controller('ProductsController', function ($scope, CONSTANS_URLS, service) {

    let getProjects = function () {
        let promiseObj = service.getData(CONSTANS_URLS.products_with_purchases);

        promiseObj.then(function (value) {
            $scope.productsData = value;
        })

    };

    console.log(CONSTANS_URLS.products_with_purchases);

    getProjects();

});


