angular.module('gifter.analysis', [])

    .controller('AnalysisCtrl', ['$state', 'stateService', 'storageService',
    	function ($state, stateService, storageService) {

    		stateService.setState($state.current.name);

    		this.storage = storageService;

    		this.backToMain = function() {
    			$state.go('main.newPresent');
    		};

    }]);