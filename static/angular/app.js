var App = angular.module('angularApp', [
    'ui.router',
    'angularApp.users',
    'angularApp.products',
    // 'angularApp.notes',
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

        // .state('notes', {
        //     url: '/angular/notes',
        //     controller: 'NotesController',
        //     templateUrl: 'static/angular/notes/view_notes_table.html'
        // })
});
