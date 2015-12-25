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
                }
    		};

        });
