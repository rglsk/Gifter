angular.module('gifter.newPresent', [])

    .controller('NewPresentCtrl', ['$state', 'stateService', '$http',
    	function ($state, stateService, $http) {

    		stateService.setState($state.current.name);

    		this.twitterName = '';
    		this.from = '';
    		this.to = '';

    		this.find = function () {
    			var url = 'http://127.0.0.1:5000/api/items/' + this.twitterName + '/';
    			$http.post(url)
    			.success(function (res) {
        			console.log(res);
        			//$state.go('main.result');
        		});
    		};

    }]);