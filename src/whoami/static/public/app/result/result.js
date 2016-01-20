angular.module('whoami.result', [])

    .controller('ResultCtrl', ['$state', 'storageService', '$http',
    	function ($state, storageService, $http) {

            this.twitterName = storageService.twitterName;
            this.person = storageService.person;
            this.category = storageService.category;

            this.saveTweet = function() {
                var url = 'http://localhost:5000/api/save/person/';
                $http.post(url, {
                    'screen_name': storageService.twitterName || '',
                    'interest_category': storageService.category || ''
                });
            };

    		this.findNew = function() {
    			$state.go('main');
    		};

    }]);