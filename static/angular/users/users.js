angular.module('angularApp.users', [
    'users.user',
    'constansApiUrls'
])
.config(function config($stateProvider){
    $stateProvider
        .state('userInformation', {
            url: '/users/:uuid',
            params: { uuid: null },
            templateUrl: 'static/angular/users/templates/user.html',
            controller: 'UserController'
        })
})

.controller('UsersController', function ($scope, $state, CONSTANS_URLS, service) {
    let getUsers = function () {
        let promiseObj = service.getData(CONSTANS_URLS.users);
        promiseObj.then(function (value) {
            $scope.usersData = value;
            console.log(CONSTANS_URLS.users);
        })
    };
    getUsers();

});


