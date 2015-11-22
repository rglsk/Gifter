angular.module('gifter.newPresent', [])

    .controller('NewPresentCtrl', ['$state', 'stateService', '$http', 'storageService',
    	function ($state, stateService, $http, storageService) {

    		stateService.setState($state.current.name);

            $http.get('http://localhost:5000/csrf/', {}).success(function (res) {
                storageService.csrf = res.token;
            });

    		this.twitterName = '';
    		this.priceSlider = {
                min: 0,
                max: 180,
                ceil: 500,
                floor: 0
            };
            this.viewReady = true;

            this.translate = function (value) {
                return value + '$';
            };

    		this.find = function () {
                that = this;
                this.viewReady = false;
    			var url = 'http://localhost:5000/api/items/' + this.twitterName + '/';
    			$http.post(url, {
                    'min_price': this.priceSlider.min || 0,
                    'max_price': this.priceSlider.max || 100,
    				'limit': 3,
                    '_csrf_token': storageService.csrf
    			}).success(function (res) {
                    storageService.twitterName = that.twitterName;
        			storageService.savePresents(res.gifts);
                    storageService.category = res.category;
                    storageService.hashtags = res.hashtags;
        			$state.go('main.result');
        		});
    		};

    }]);