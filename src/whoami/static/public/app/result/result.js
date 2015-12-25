angular.module('whoami.result', [])

    .controller('ResultCtrl', ['$state', 'storageService', '$http',
    	function ($state, storageService, $http) {

            this.twitterName = storageService.twitterName;
            this.person = storageService.person;
            this.category = storageService.category;

    		this.findNew = function() {
    			$state.go('main');
    		};

    }]);