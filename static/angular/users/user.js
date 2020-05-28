angular.module('users.user', [

])

.controller('UserController', function ($scope, $stateParams, service, CONSTANS_URLS) {
    let getUserData = function (url, data) {
        let promiseObj = service.getData(url);
        promiseObj.then(function (value) {
            $scope[data] = value;
        })
    };

    getUserData(CONSTANS_URLS.orders_for_user + $stateParams['uuid'], 'orders');
    getUserData(CONSTANS_URLS.user + $stateParams['uuid'], 'user');
    getUserData(CONSTANS_URLS.user_purchased_products + $stateParams['uuid'], 'products');
    getUserData(CONSTANS_URLS.user_comments + $stateParams['uuid'], 'comments');

    const COLORS = {
        Orders : '#ff4f4f',
        Products : '#a39d9d',
        Comments: '#55b5fa',
    };

    const STATUSES = {
        Orders : 'Всего заказов',
        Products : 'Куплень товаров',
        Comments : 'Комментарии',
    };

    function setParams(statusData){
        return {
            labels: [
                STATUSES.Orders,
                STATUSES.Products,
                STATUSES.Comments,
            ],
            datasets: [
                {
                    data: [statusData[STATUSES.Orders],
                        statusData[STATUSES.Products],
                        statusData[STATUSES.Comments],
                    ],
                    backgroundColor: [COLORS.Orders, COLORS.Products, COLORS.Comments],
                }
            ]
        };
	}

	$scope.createChart = function(orders, products, comments) {

        let donutChartCanvas = document.getElementById("donutChart").getContext('2d');

        let statusData = {
            'Всего заказов' : orders,
            'Куплень товаров' : products,
            'Комментарии' : comments
        };

        let donutData = setParams(statusData);

        let donutOptions = {
            maintainAspectRatio: false,
            responsive: true,
        };

        let donutChart = new Chart(donutChartCanvas, {
            type: 'doughnut',
            data: donutData,
            options: donutOptions
        });
    }
});