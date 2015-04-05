angular.module('gifter.route', ['gifter.viewComponents.route'])

    .config(function ($stateProvider, ViewComponents) {

        $stateProvider
            .state('main', {
                url: '',
                views: {
                    'panel@': ViewComponents.panel
                }
            });
    });