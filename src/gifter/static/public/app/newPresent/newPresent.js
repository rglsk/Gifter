angular.module('gifter.newPresent', [])

    .controller('NewPresentCtrl', ['$state', 'stateService', '$http', 'storageService',
    	function ($state, stateService, $http, storageService) {

    		stateService.setState($state.current.name);

    		this.twitterName = '';
    		this.priceSlider = {
                min: 0,
                max: 180,
                ceil: 500,
                floor: 0
            };
            this.viewReady = true;
            this.error = '';

            this.translate = function (value) {
                return value + '$';
            };

            this.findNew = function () {
                this.error = '';
                this.viewReady = true;
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
                    if (res.gifts) {
                        storageService.twitterName = that.twitterName;
            			storageService.savePresents(res.gifts);
                        storageService.category = res.category;
                        storageService.hashtags = res.hashtags;
            			$state.go('main.result');
                    } else {
                        that.viewReady = true;
                        switch (res.error) {
                            case 'user_not_found':
                                that.error = "We are sorry, this user doesn't exist. Please, check another one.";
                                break;
                            case 'presents_not_found':
                                that.error = "We are sorry, we haven't found suitable presents for given person. Please, check antoher one.";
                                break;
                            case 'no_tweets':
                                that.error = "We are sorry, this user has no tweets. Please, check another one.";
                                break;
                            default:
                                that.error = "We are sorry, some errors occurred. Please, try again.";
                        }
                    }
        		});
    		};

    }]);