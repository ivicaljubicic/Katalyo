'use strict';

// declare modules
angular.module('Authentication', []);
 
angular.module('indexKatalyo', [
    'Authentication',
    'ngRoute',
    'ngCookies'
]).controller('authCtrl', function($scope) {
        // $scope.navbar = "/static/angularTemplates/navbar.html";
       // $scope.title = "Katalyo | Login";
    })
.controller('navbarCtrl', function($scope) {
        $scope.navbar = "/static/angularTemplates/navbar.html";
    })

.controller('titleCtrl', function($scope) {
        $scope.title = "Katalyo | Home";
    })
.config(['$routeProvider', function ($routeProvider) {
 
    $routeProvider
        .when('/login', {
            controller: 'LoginController',
            templateUrl: '/static/angularTemplates/login.html'
        })
  
        .when('/', {
            controller: 'HomeController',
            templateUrl: '/static/angularTemplates/resource-def.html'
        })
  
        .otherwise({ redirectTo: '/login' });
}])
  
.run(['$rootScope', '$location', '$cookieStore', '$http',
    function ($rootScope, $location, $cookieStore, $http) {
        // keep user logged in after page refresh
        $rootScope.globals = $cookieStore.get('globals') || {};
        if ($rootScope.globals.currentUser) {
            $http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentUser.authdata; // jshint ignore:line
        }
  
        $rootScope.$on('$locationChangeStart', function (event, next, current) {
            // redirect to login page if not logged in
            if ($location.path() !== '/login' && !$rootScope.globals.currentUser) {
                $location.path('/login');
            }
        });
    }]);