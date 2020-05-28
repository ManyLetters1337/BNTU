angular.module('angularApp.orders', [
    'orders.order',
    'constansApiUrls'
])

.config(function config($stateProvider) {
    $stateProvider
        .state('orderInformation', {
            url: '/orders/:uuid',
            params: { uuid : null },
            controller: 'OrderController',
            templateUrl: 'static/angular/orders/templates/order.html'
        })

})

.controller('OrdersController', function ($scope, CONSTANS_URLS, service) {

    let getOrders = function (url, data) {
        let promiseObj = service.getData(url, data);

        promiseObj.then(function (value) {
            $scope[data] = value;
        })

    };

    $scope.status = false;

    getOrders(CONSTANS_URLS.pending_orders, 'ordersData');
    getOrders(CONSTANS_URLS.history_orders, 'ordersHistory');

    console.log()

});


