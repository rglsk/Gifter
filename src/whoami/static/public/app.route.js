angular.module('whoami.route', ['whoami.viewComponents.route'])

    .config(function ($stateProvider, ViewComponents) {

        $stateProvider
            .state('main', {
                url: '',
                views: {
                	'content@': {
                        templateUrl: 'app/start/start.html',
                        controller: 'StartCtrl as StartCtrl'
                    },
                    'panel@': ViewComponents.panel
                }
            });
    });