angular.module('gifter.result', [])

    .controller('ResultCtrl', ['$state', 'stateService', 'storageService',
    	function ($state, stateService, storageService) {

    		stateService.setState($state.current.name);

            this.presents = storageService.presents;

    		this.seeMore = function() {
    			$state.go('main.analysis');
    		};

    }]);