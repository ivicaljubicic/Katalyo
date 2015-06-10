'use strict';

// declare modules
angular.module('Authentication', []);
 
angular.module('Katalyo', [
    'Authentication',
    'ui.router',
    'ngCookies'
])

.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/login');
 
    $stateProvider
        .state('login', {
            url:'/login',
            controller: 'loginCtrl',
            templateUrl: '/static/modules/0002_auth/angularTemplates/login.html'
        })
        .state('resourceDef', {
            url:'/resource-def',
            controller: 'resourceDefCtrl',
            templateUrl: '/static/modules/0003_resourceDef/angularTemplates/resource-def.html'
        })
 
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