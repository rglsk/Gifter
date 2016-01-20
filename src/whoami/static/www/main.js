var app = angular.module('whoami', [
    
    'ui.router',
    'ui.bootstrap',
    'whoami.route',
    
    'whoami.start',

    'whoami.result',
    'whoami.result.route',

    'whoami.viewComponents.panel',

    'whoami.services.storageService',
]);

angular.module('whoami.route', ['whoami.viewComponents.route'])

    .config(function ($stateProvider, ViewComponents) {

        $stateProvider
            .state('main', {
                url: '',
                views: {
                	'content@': {
                        templateUrl: 'app/start/start.html',
                        controller: 'StartCtrl as StartCtrl'
                    },
                    'panel@': ViewComponents.panel
                }
            });
    });
angular.module('whoami.services.storageService', [])

    .service('storageService', function () {

    		var person = {
                    'name': '',
                    'desc': '',
                    'imgUrl': '',
                },
                category = '',
                twitterName = '',
                savePerson = function(p) {
                    person = p;
                };

    		return {
                savePerson: savePerson,
    			get name() {
    				return name;
    			},
                get desc() {
                    return desc;
                },
                get imgUrl() {
                    return imgUrl;
                },
                set twitterName(name) {
                    twitterName = name;
                },
                get twitterName() {
                    return twitterName;
                },
                set category(cat) {
                    category = cat;
                },
                get category() {
                    return category;
                },
                get person() {
                    return person;
                }
    		};

        });

angular.module('whoami.viewComponents.panel', [])

    .controller('PanelCtrl', [
    	function () {

        }]);

angular.module('whoami.viewComponents.route', [])

    .constant('ViewComponents', {

        panel: {
            templateUrl: 'app/common/viewComponents/panel/panel.html',
            controller: 'PanelCtrl as PanelCtrl'
        }

    }

);

angular.module('whoami.result', [])

    .controller('ResultCtrl', ['$state', 'storageService', '$http',
    	function ($state, storageService, $http) {

            this.twitterName = storageService.twitterName;
            this.person = storageService.person;
            this.category = storageService.category;

            this.saveTweet = function() {
                var url = 'http://localhost:5000/api/save/person/';
                $http.post(url, {
                    'screen_name': storageService.twitterName || '',
                    'interest_category': storageService.category || ''
                });
            };

    		this.findNew = function() {
    			$state.go('main');
    		};

    }]);
angular.module('whoami.result.route', [])

    .config(function ($stateProvider) {

        $stateProvider
            .state('main.result', {
                url: '/result',
                views: {
                    'content@': {
                        templateUrl: 'app/result/result.html',
                        controller: 'ResultCtrl as ResultCtrl'
                    }
                }
            });
    });
angular.module('whoami.start', [])

    .controller('StartCtrl', ['$state', '$http', 'storageService',
    	function ($state, $http, storageService) {

    		this.twitterName = '';
            this.breakFunction = false;
            this.viewReady = true;
            this.error = '';

            this.findNew = function () {
                this.error = '';
                this.twitterName = '';
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