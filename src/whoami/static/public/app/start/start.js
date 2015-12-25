angular.module('whoami.start', [])

    .controller('StartCtrl', ['$state', '$http', 'storageService',
    	function ($state, $http, storageService) {

    		this.twitterName = '';
            this.breakFunction = false;
            this.viewReady = true;
            this.error = '';

            this.findNew = function () {
                this.error = '';
                this.viewReady = true;
            };

            this.reset = function () {
                this.viewReady = true;
                this.breakFunction = true;
            };

    		this.find = function () {
                that = this;
                this.breakFunction = false;
                this.viewReady = false;
    			var url = 'http://localhost:5000/api/person/' + this.twitterName + '/';
    			$http.post(url, {}).success(function (res) {
                    if (!that.breakFunction) {
                        if (res.person) {
                            storageService.twitterName = that.twitterName;
                			storageService.savePerson(res.person);
                            storageService.category = res.category;
                			$state.go('main.result');
                        } else {
                            that.viewReady = true;
                            switch (res.error) {
                                case 'user_not_found':
                                    that.error = "We are sorry, this user doesn't exist. Please, check another one.";
                                    break;
                                case 'person_not_found':
                                    that.error = "We are sorry, we haven't found right matching for this user. Please, check antoher one.";
                                    break;
                                case 'no_tweets':
                                    that.error = "We are sorry, this user has no tweets. Please, check another one.";
                                    break;
                                default:
                                    that.error = "We are sorry, some errors occurred. Please, try again.";
                            }
                        }
                    }
        		});
    		};

    }]);