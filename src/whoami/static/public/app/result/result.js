angular.module('whoami.result', [])

    .controller('ResultCtrl', ['$state', 'storageService', '$http',
    	function ($state, storageService, $http) {

            this.twitterName = storageService.twitterName;
            this.person = storageService.person;
            // this.twitterName = 'bckatarzyna';
            // this.person = {
            // 	'name': 'Khaleesi',
            // 	'desc': 'You like dragons or another stupid staff chosen by our overfitted algorithm. But it\'s great, everybody wants to be her! Omg this app is so cool.',
            // 	'imgUrl': '/assets/images/khaleesi.jpg'
            // };
            this.category = storageService.category;

    		this.findNew = function() {
    			$state.go('main');
    		};

    }]);