angular.module('whoami.result.route', [])

    .config(function ($stateProvider) {

        $stateProvider
            .state('main.result', {
                url: '/result',
                views: {
                    'content@': {
                        templateUrl: 'app/result/result.html',
                        controller: 'ResultCtrl as ResultCtrl'
                    }
                }
            });
    });