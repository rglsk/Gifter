var app = angular.module("gifter", [
    
    'ui.router',
    'ui.bootstrap',
    'rzModule',
    'gifter.route',
    
    'gifter.newPresent',
    'gifter.newPresent.route',

    'gifter.result',
    'gifter.result.route',

    'gifter.viewComponents.panel',

    'gifter.services.stateService',
    'gifter.services.storageService',
])

    .run(function($rootScope, $modalStack) {
        $modalStack. dismissAll();
    });