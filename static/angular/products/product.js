angular.module('products.product', [

])

.controller('ProductController', function ($http, $scope, $stateParams, CONSTANS_URLS, service) {
    function getInformation (url, data) {
        let promiseObj = service.getData(url);
        promiseObj.then(function (value){
            $scope[data] = value;
        })
    }

    getInformation(CONSTANS_URLS.product + $stateParams['uuid'], 'product');

    getInformation(CONSTANS_URLS.orders_for_product + $stateParams['uuid'], 'orders')

    function getCanvas() {
        return document.getElementById('donutChart').getContext('2d');
    }

    const COLORS = {
        Open : '#ff4f4f',
        Closed : '#a39d9d',
        InProgress: '#55b5fa',
        Resolved : '#6bfa55'
    };

    const STATUSES = {
        Open : 'Open',
        Closed : 'Closed',
        InProgress : 'In Progress',
        Resolved : 'Resolved'
    };

    function setParams(statusData){
        return {
            labels: [
                STATUSES.Open,
                STATUSES.InProgress,
                STATUSES.Resolved,
                STATUSES.Closed,
            ],
            datasets: [
                {
                    data: [statusData[STATUSES.Open],
                        statusData[STATUSES.InProgress],
                        statusData[STATUSES.Resolved],
                        statusData[STATUSES.Closed]
                    ],
                    backgroundColor: [COLORS.Open, COLORS.InProgress, COLORS.Resolved, COLORS.Closed],
                }
            ]
        };
	}

	function createChart(statusData) {

        statusData = {
            'Open' : 1,
            'Closed' : 2,
            'In Progress' : 3,
            'Resolved' : 4
        };

        let donutChartCanvas = getCanvas();

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

    let getDataForStatistic = function () {

    };

    // createChart(getDataForStatistic());

});