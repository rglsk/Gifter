angular.module('gifter.result', [])

    .controller('ResultCtrl', ['$state', 'stateService', 'storageService',
    	function ($state, stateService, storageService) {

    		stateService.setState($state.current.name);
    		this.slider = 1;

            this.presents = storageService.presents;

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

            // this.presents = [
            // 	{
            // 		'id': 0,
            // 		'name': 'Great present',
            // 		'img': 'assets/images/xmas.png',
            // 		'price': '40.00USD',
            // 		'hidden': 1
            // 	},
            // 	{
            // 		'id': 1,
            // 		'name': 'Even better present',
            // 		'img': 'assets/images/xmas.png',
            // 		'price': '30.00USD',
            // 		'hidden': 0
            // 	},
            // 	{
            // 		'id': 2,
            // 		'name': 'So this is completely the best option',
            // 		'img': 'assets/images/xmas.png',
            // 		'price': '59.99USD',
            // 		'hidden': 1
            // 	}
            // ];

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

    		this.seeMore = function() {
    			$state.go('main.analysis');
    		};

    }]);