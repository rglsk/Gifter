var app = angular.module("gifter", [
    
    'ui.router',
    'ui.bootstrap',
    'rzModule',
    'gifter.route',
    
    'gifter.newPresent',
    'gifter.newPresent.route',

    'gifter.result',
    'gifter.result.route',

    'gifter.viewComponents.panel',

    'gifter.services.stateService',
    'gifter.services.storageService',
])

    .run(function($rootScope, $modalStack) {
        $modalStack. dismissAll();
    });
angular.module('gifter.route', ['gifter.viewComponents.route'])

    .config(function ($stateProvider, ViewComponents) {

        $stateProvider
            .state('main', {
                url: '',
                views: {
                	'content@': {
                        templateUrl: 'app/newPresent/newPresent.html',
                        controller: 'NewPresentCtrl as NewPresentCtrl'
                    },
                    'panel@': ViewComponents.panel
                }
            });
    });
angular.module('gifter.services.stateService', [])

    .service('stateService', function () {

    		var state,
    			setState = function (s) {
    				switch (s) {
    					case 'main.newPresent':
    						state = 'New present';
    						break;
    					case 'main.result':
    						state = 'Result';
    						break;
                        case 'main.analysis':
                            state = 'Analysis';
                            break;
    					default:
    						state = 'Gifter';
    					}
    			};

    		return {
    			setState: setState,
    			get state() {
    				return state;
    			}
    		};

        });

angular.module('gifter.services.storageService', [])

    .service('storageService', function () {

    		var presents = [],
                hashtags = [],
                twitterName = ''
                category = '',
                savePresents = function(gifts) {
                    presents = [];
                    gifts.forEach(function(gift) {
                        presents.push({
                            'name': gift.title,
                            'img': gift.pictureURLSuperSize,
                            'price': gift.sellingStatus.convertedCurrentPrice.value +
                            gift.sellingStatus.convertedCurrentPrice._currencyId,
                            'url': gift.viewItemURL,
                            'category': gift.primaryCategory.categoryName
                        });
                    });
                };

    		return {
                savePresents: savePresents,
    			get presents() {
    				return presents;
    			},
                set hashtags(h) {
                    hashtags = h;
                },
                get hashtags() {
                    return hashtags;
                },
                set twitterName(t) {
                    twitterName = t;
                },
                get twitterName() {
                    return twitterName;
                },
                set category(cat) {
                    category = cat;
                },
                get category() {
                    return category;
                }
    		};

        });

angular.module('gifter.viewComponents.panel', [])

    .controller('PanelCtrl', ['stateService',
    	function (stateService) {

    		this.stateService = stateService;

        }]);

angular.module('gifter.viewComponents.route', [])

    .constant('ViewComponents', {

        panel: {
            templateUrl: 'app/common/viewComponents/panel/panel.html',
            controller: 'PanelCtrl as PanelCtrl'
        }

    }

);

angular.module('gifter.newPresent', [])

    .controller('NewPresentCtrl', ['$state', 'stateService', '$http', 'storageService',
    	function ($state, stateService, $http, storageService) {

    		stateService.setState($state.current.name);

    		this.twitterName = '';
            this.breakFunction = false;
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

            this.reset = function () {
                this.viewReady = true;
                this.breakFunction = true;
            };

    		this.find = function () {
                that = this;
                this.breakFunction = false;
                this.viewReady = false;
    			var url = 'http://localhost:5000/api/items/' + this.twitterName + '/';
    			$http.post(url, {
                    'min_price': this.priceSlider.min || 0,
                    'max_price': this.priceSlider.max || 100,
    				'limit': 3,
                    '_csrf_token': storageService.csrf
    			}).success(function (res) {
                    if (!that.breakFunction) {
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
                    }
        		});
    		};

    }]);
angular.module('gifter.newPresent.route', [])

    .config(function ($stateProvider) {

        $stateProvider
            .state('main.newPresent', {
                url: '/newPresent',
                views: {
                    'content@': {
                        templateUrl: 'app/newPresent/newPresent.html',
                        controller: 'NewPresentCtrl as NewPresentCtrl'
                    }
                }
            });
    });
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
                    'interest_category': storageService.category || ''
                }).success(function (res) {              
                    $window.open(present.url, '_blank');
                });
            };

    		this.findNew = function() {
    			$state.go('main.newPresent');
    		};

    }]);
angular.module('gifter.result.route', [])

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