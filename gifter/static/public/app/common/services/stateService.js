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
