module.exports = function (grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        jshint: {
            all: [
                'Gruntfile.js',
                'js/main.js',
                'js/controllers/*.js',
                'js/factories/*.js',
                'js/services/*.js',
                'js/directives/*.js'
            ]
        },
        concat: {
            dist: {
                src: [
                    'bower_components/angularjs/angular.js',
                    'bower_components/angular-route/angular-route.js',
                    'bower_components/lodash/lodash.js',
                    'bower_components/restangular/dist/restangular.js',
                    'bower_components/angular-local-storage/dist/angular-local-storage.js',
                    'js/main.js',
                    'js/controllers/*.js',
                    'js/factories/*.js',
                    'js/services/*.js',
                    'js/directives/*.js'
                ],
                dest: 'js/build/production.js'
            }
        },
        ngAnnotate: {
            options: {
                singleQuotes: true
            },
            target: {
                files: [
                    {
                        expand: true,
                        src: ['js/build/production.js'],
                        ext: '.annotated.js',
                        extDot: 'last'
                    }
                ]
            }
        },
        uglify: {
            build: {
                src: 'js/build/production.annotated.js',
                dest: 'js/build/production.min.js'
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-ng-annotate');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    grunt.registerTask('default', ['jshint', 'concat', 'ngAnnotate', 'uglify']);

};