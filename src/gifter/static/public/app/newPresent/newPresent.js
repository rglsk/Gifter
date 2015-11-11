angular.module('gifter.newPresent', [])

    .controller('NewPresentCtrl', ['$state', '$modal', 'stateService', '$http', 'storageService',
    	function ($state, $modal, stateService, $http, storageService) {

    		stateService.setState($state.current.name);

    		this.twitterName = '';
    		this.priceSlider = {
                min: 100,
                max: 180,
                ceil: 500,
                floor: 0
            };
            this.modalInstance = '';
            this.viewReady = true;

            this.translate = function (value) {
                return value + '$';
            };

            this.openModal = function (size) {
                this.modalInstance = $modal.open({
                    templateUrl: 'app/common/viewComponents/modal/modal.html'
                });
            };

    		this.find = function () {
                // $state.go('main.result');
                that = this;
                this.viewReady = false;
                that.openModal();
    			var url = 'http://localhost:5000/api/items/' + this.twitterName + '/';
    			$http.post(url, {
                    'min_price': this.priceSlider.min || 0,
                    'max_price': this.priceSlider.max || 100,
    				'limit': 3
    			}).success(function (res) {
                    storageService.twitterName = that.twitterName;
        			storageService.savePresents(res.gifts);
                    storageService.hashtags = res.hashtags;
                    that.modalInstance.close();
        			$state.go('main.result');
        		});
    		};

    }]);