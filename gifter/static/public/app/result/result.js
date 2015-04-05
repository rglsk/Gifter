angular.module('gifter.result', [])

    .controller('ResultCtrl', ['$state', 'stateService',
    	function ($state, stateService) {

    		stateService.setState($state.current.name);

    }]);