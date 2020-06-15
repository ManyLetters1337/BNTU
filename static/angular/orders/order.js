angular.module('orders.order', [

])

.controller('OrderController', function ($http, $scope, $stateParams, CONSTANS_URLS, service, $location) {
    function getInformation(url, data) {
        let promiseObj = service.getData(url);
        promiseObj.then(function (value){
            $scope[data] = value;
        })
    }

    $scope.product_url = CONSTANS_URLS.product_view;
    getInformation(CONSTANS_URLS.product_for_order + $stateParams['uuid'] + `/products`, 'products');

    getInformation(CONSTANS_URLS.order_information + $stateParams['uuid'], 'order');

    $scope.changeStatus = function () {
        let xhr = new XMLHttpRequest();

        let body = 'uuid=' + encodeURIComponent($scope.order['uuid']);

        xhr.open("POST", CONSTANS_URLS.accept_order + $scope.order['uuid'] + `/accept`, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        xhr.send(body);

        $location.path('/orders');
    }

});