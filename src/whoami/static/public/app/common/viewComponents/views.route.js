angular.module('whoami.viewComponents.route', [])

    .constant('ViewComponents', {

        panel: {
            templateUrl: 'app/common/viewComponents/panel/panel.html',
            controller: 'PanelCtrl as PanelCtrl'
        }

    }

);
