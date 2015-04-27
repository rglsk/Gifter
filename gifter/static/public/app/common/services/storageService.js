angular.module('gifter.services.storageService', [])

    .service('storageService', function () {

    		var presents = [],
                savePresents = function(gifts) {
                    presents = [];
                    gifts.forEach(function(gift) {
                        presents.push({
                            'name': gift.title,
                            'img': gift.galleryURL,
                            'price': gift.sellingStatus.convertedCurrentPrice.value +
                            gift.sellingStatus.convertedCurrentPrice._currencyId 
                        });
                    });
                };

    		return {
                savePresents: savePresents,
    			get presents() {
    				return presents;
    			}
    		};

        });
