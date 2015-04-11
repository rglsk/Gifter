angular.module('gifter.newPresent.route', [])

    .config(function ($stateProvider) {

        $stateProvider
            .state('main.newPresent', {
                url: '/newPresent',
                views: {
                    'content@': {
                        templateUrl: 'app/newPresent/newPresent.html',
                        controller: 'NewPresentCtrl as NewPresentCtrl'
                    }
                }
            });
    });