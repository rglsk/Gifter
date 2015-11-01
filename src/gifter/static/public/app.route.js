angular.module('gifter.route', ['gifter.viewComponents.route'])

    .config(function ($stateProvider, ViewComponents) {

        $stateProvider
            .state('main', {
                url: '',
                views: {
                	'content@': {
                        templateUrl: 'app/newPresent/newPresent.html',
                        controller: 'NewPresentCtrl as NewPresentCtrl'
                    },
                    'panel@': ViewComponents.panel
                }
            });
    });