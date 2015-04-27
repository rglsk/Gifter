angular.module('gifter.newPresent', [])

    .controller('NewPresentCtrl', ['$state', 'stateService', '$http', 'storageService',
    	function ($state, stateService, $http, storageService) {

    		stateService.setState($state.current.name);

    		this.twitterName = '';
    		this.from = '';
    		this.to = '';

    		this.find = function () {
    			var url = 'http://127.0.0.1:5000/api/items/' + this.twitterName + '/';
    			$http.post(url, {
    				'min_price': this.from || 0,
    				'max_price': this.to || 100,
    				'limit': 4
    			}).success(function (res) {
        			storageService.savePresents(res.gifts);
        			$state.go('main.result');
        		});
    		};

    }]);