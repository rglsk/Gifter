angular.module('gifter.newPresent', [])

    .controller('NewPresentCtrl', ['$state', 'stateService',
    	function ($state, stateService) {

    		stateService.setState($state.current.name);

    		this.find = function () {
    			$state.go('main.result');
    		};

    }]);