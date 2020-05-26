angular.module('users.user', [

])

.controller('UserController', function ($scope, $stateParams, service, CONSTANS_URLS) {
    let getUserData = function (url, data) {
        let promiseObj = service.getData(url);
        promiseObj.then(function (value) {
            $scope[data] = value;
        })
    };

    $scope.selector = true;

    if ($scope.selector){
        getUserData(CONSTANS_URLS.orders_for_user + $stateParams['uuid'], 'orders');
        console.log(CONSTANS_URLS.orders_for_user + $stateParams['uuid'])
    }
    else {
        getUserData(CONSTANS_URLS.user + $stateParams['uuid'], 'orders');
    }

    getUserData(CONSTANS_URLS.user + $stateParams['uuid'], 'user');

});