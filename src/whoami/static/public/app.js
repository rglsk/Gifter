var app = angular.module('whoami', [
    
    'ui.router',
    'ui.bootstrap',
    'whoami.route',
    
    'whoami.start',

    'whoami.result',
    'whoami.result.route',

    'whoami.viewComponents.panel',

    'whoami.services.storageService',
]);
