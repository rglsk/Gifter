module.exports = function(grunt) {
 
	require('load-grunt-tasks')(grunt);

 	grunt.initConfig({
        paths: {
            public: 'public',
            dist: 'www'
        },

        jshint: {
            options: {
                jshintrc: '.jshintrc'
            },
            files: [
              '<%= paths.public %>/**/{,*/}*.js'
            ]
        },

        clean: {
            all: {
                src: [
                    '<%= paths.dist %>'
                ]
            }
        },

        concat: {
                js: {
                    src: '<%= paths.public %>/**/{,*/}*.js',
                    dest: '<%= paths.dist %>/main.js'
                },
                css: {
                    src: '<%= paths.public %>/**/{,*/}*.css',
                    dest: '<%= paths.dist %>/main.css'
                }
        },

        copy: {
            components: {
                files: [
                    {
                        expand: true,
                        dest: '<%= paths.dist %>',
                        src: 'bower_components/**/*'
                    },
                    {
                        expand: true,
                        cwd: '<%= paths.public %>',
                        dest: '<%= paths.dist %>',
                        src: 'common/images/*'
                    }
                ]
            },
            html: {
                files: [
                    {
                        expand: true,
                        cwd: '<%= paths.public %>',
                        dest: '<%= paths.dist %>',
                        src: [
                            'app/{,*/}*.html',
                            'index.html'
                        ]
                    }
                ]
            }
        },

        connect: {
            options: {
                port: 3000,
                hostname: 'localhost',
                livereload: 12345
            },
            livereload: {
                options: {
                    open: {
                        target: 'http://localhost:3000/#/newPresent',
                        appName: 'google-chrome'
                    },
                    base: [
                        '<%= paths.dist %>'
                    ]
                }
            }
        },

        watch: {
            js: {
                files: [
                    '<%= paths.public %>/**/{,*/}*.js',
                    '!<%= paths.public %>/main.js'
                ],
                tasks: [
                    'jshint',
                    'concat:js'
                    ]
            },
            css: {
                files: [
                    '<%= paths.public %>/**/{,*/}*.css',
                    '!<%= paths.public %>/main.css'
                ],
                tasks: [
                    'concat:css'
                ]
            },
            html: {
                files: [
                    '<%= paths.public %>/**/{,*/}*.html'
                ],
                tasks: [
                    'copy:html'
                ]
            },
            all: {
                files: [
                    '<%= paths.public %>/**/{,*/}*.js',
                    '<%= paths.public %>/**/{,*/}*.html',
                    '<%= paths.public %>/**/{,*/}*.css'
                ],
                options: {
                    livereload: 12345
                }
          }
        }

    });

    grunt.registerTask('hint', function () {
        var taskList = [
            'jshint'
        ];
        grunt.task.run(taskList);
    });

    grunt.registerTask('serve', function () {
        var taskList = [
            'clean',
            'concat',
            'copy',
            'connect:livereload',
            'watch'
        ];
        grunt.task.run(taskList);
    });
};