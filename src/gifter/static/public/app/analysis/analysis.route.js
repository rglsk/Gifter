angular.module('gifter.analysis.route', [])

    .config(function ($stateProvider) {

        $stateProvider
            .state('main.analysis', {
                url: '/analysis',
                views: {
                    'content@': {
                        templateUrl: 'app/analysis/analysis.html',
                        controller: 'AnalysisCtrl as AnalysisCtrl'
                    }
                }
            });
    });