'use strict';

// declare module
 
angular.module('Katalyo', [
    'Authentication',
    'ngRoute',
    'ngCookies'
])

.controller('navbarCtrl', function($scope) {
        $scope.navbar = "/static/modules/0001_index/angularTemplates/navbar.html";
    })
.controller('layoutCtrl', function($scope) {
        $scope.layout = "/static/modules/0001_index/angularTemplates/layout.html";
    })

.controller('titleCtrl', function($scope) {
        $scope.title = "Katalyo | Home";
    }

);