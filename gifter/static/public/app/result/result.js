angular.module('gifter.result', [])

    .controller('ResultCtrl', ['$state', 'stateService',
    	function ($state, stateService) {

    		stateService.setState($state.current.name);

    		this.seeMore = function() {
    			$state.go('main.analysis');
    		};

    		this.presents = [
    			{
    				name: 'Ultra Funny Thing',
    				img: 'assets/images/present.jpg',
    				price: '50.00$'
    			},
    			{
    				name: 'Best present ever',
    				img: 'assets/images/present.jpg',
    				price: '31.46$'
    			},
    			{
    				name: 'Another present name',
    				img: 'assets/images/present.jpg',
    				price: '20.32$'
    			},
    			{
    				name: 'Present once again',
    				img: 'assets/images/present.jpg',
    				price: '17.89$'
    			}
    		];

    }]);