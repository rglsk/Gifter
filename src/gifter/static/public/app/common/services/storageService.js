angular.module('gifter.services.storageService', [])

    .service('storageService', function () {

    		var presents = [],
                hashtags = [],
                twitterName = '',
                csrf = '';
                category = '';
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
                set csrf(c) {
                    csrf = c;
                },
                get csrf() {
                    return csrf;
                },
                set category(cat) {
                    category = cat;
                },
                get category() {
                    return category;
                }
    		};

        });
