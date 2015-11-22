angular.module('gifter.result', [])

    .controller('ResultCtrl', ['$state', 'stateService', 'storageService', '$window', '$http',
    	function ($state, stateService, storageService, $window, $http) {

    		stateService.setState($state.current.name);
    		this.slider = 1;

            this.presents = storageService.presents;
            this.category = storageService.category;

            var i = 0;
            this.presents.forEach(function(present) {
            	present.id = i;
            	if (i == 1) {
            		present.hidden = 0;
            	} else {
            		present.hidden = 1;
            	}
            	i++;
            });

            this.changeClass = function(present) {
            	this.slider = present.id;
            	for (i = 0; i < this.presents.length; i++) {
            		if (this.presents[i].id == present.id) {
            			this.presents[i].hidden = 0;
            		} else {
            			this.presents[i].hidden = 1;
            		}
            	}
            };

            this.seePresent = function ($event, present) {
                var url = 'http://localhost:5000/api/save/';
                $http.post(url, {
                    'screen_name': storageService.twitterName || '',
                    'gift_category': present.category || '',
                    'interest_category': storageService.category || '',
                    '_csrf_token': storageService.csrf
                }).success(function (res) {
                    // $event.stopPropagation();                
                   $window.open(present.url, '_blank');
                });
            };

    		this.findNew = function() {
    			$state.go('main.newPresent');
    		};

    }]);