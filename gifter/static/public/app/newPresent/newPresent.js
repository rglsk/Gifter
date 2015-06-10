angular.module('gifter.newPresent', [])

    .controller('NewPresentCtrl', ['$state', '$modal', 'stateService', '$http', 'storageService',
    	function ($state, $modal, stateService, $http, storageService) {

    		stateService.setState($state.current.name);

    		this.twitterName = '';
    		this.from = '';
    		this.to = '';
            this.modalInstance = '';

            this.openModal = function (size) {
                this.modalInstance = $modal.open({
                  templateUrl: 'app/common/viewComponents/modal/modal.html'
                });
            };

    		this.find = function () {
                that = this;
                that.openModal();
    			var url = '/api/items/' + this.twitterName + '/';
    			$http.post(url, {
    				'min_price': this.from || 0,
    				'max_price': this.to || 100,
    				'limit': 4
    			}).success(function (res) {
                    storageService.twitterName = that.twitterName;
        			storageService.savePresents(res.gifts);
                    storageService.hashtags = res.hashtags;
                    that.modalInstance.close();
        			$state.go('main.result');
        		});
    		};

    }]);