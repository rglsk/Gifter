var app = angular.module("gifter", [
    
    'ui.router',
    'gifter.route',
    
    'gifter.newPresent',
    'gifter.newPresent.route',

    'gifter.result',
    'gifter.result.route',

    'gifter.analysis',
    'gifter.analysis.route',

    'gifter.viewComponents.panel',

    'gifter.services.stateService'

]);