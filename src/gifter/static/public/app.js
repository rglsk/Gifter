var app = angular.module("gifter", [
    
    'ui.router',
    'ui.bootstrap',
    'gifter.route',
    
    'gifter.newPresent',
    'gifter.newPresent.route',

    'gifter.result',
    'gifter.result.route',

    'gifter.analysis',
    'gifter.analysis.route',

    'gifter.viewComponents.panel',

    'gifter.services.stateService',
    'gifter.services.storageService'

])

    .run(function($rootScope, $modalStack) {
        $modalStack. dismissAll();
    });