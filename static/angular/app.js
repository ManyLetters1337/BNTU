var App = angular.module('angularApp', [
    'ui.router',
    'angularApp.users',
    'angularApp.products',
    'angularApp.orders',
    // 'angularApp.statistics'
]);

angular.module('angularApp')
.config(function config($stateProvider, $locationProvider) {

    $stateProvider
        // .state('statistics', {
        //     url: '/',
        //     controller: 'StatisticController',
        //     templateUrl: 'static/angular/statistics/statistics.html'
        // })
        .state('users', {
            url: '/users',
            controller: 'UsersController',
            templateUrl: 'static/angular/users/templates/users.html'
        })

        .state('products', {
            url: '/products',
            controller: 'ProductsController',
            templateUrl: 'static/angular/products/templates/products.html'
        })

        .state('orders', {
            url: '/orders',
            controller: 'OrdersController',
            templateUrl: 'static/angular/orders/templates/orders.html'
        })
});
