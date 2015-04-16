angular.module('gifter.analysis', [])

    .controller('AnalysisCtrl', ['$state', 'stateService',
    	function ($state, stateService) {

    		stateService.setState($state.current.name);

    }]);