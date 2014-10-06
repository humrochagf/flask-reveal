# -*- coding: utf-8 -*-
import os
import argparse

from flask_reveal.app import FlaskReveal


class Start(argparse.ArgumentParser):
    info = ({
        'prog': 'start',
        'description': 'starts a Flask Reveal presentation',
    })

    def __init__(self):
        super().__init__(**self.info)

        self.path = os.getcwd()
        self.media = None
        self.config = None
        self.debug = False
        self.add_argument('path', nargs='?', default=self.path)
        self.add_argument('-m', '--media',  default=self.media)
        self.add_argument('-c', '--config', default=self.config)
        self.add_argument('-d', '--debug', action='store_true')

    def parse_args(self, args=None, namespace=None):
        super().parse_args(args, self)
        
        # Check for presentation root
        if os.path.isdir(self.path):
            self.path = os.path.abspath(self.path)
            
            # Check for media root
            if not self.media:
                self.media = os.path.join(self.path, 'img')
                
            if os.path.isdir(self.media):
                # Check for configuration file
                if not self.config:
                    self.config = os.path.join(self.path, 'config.py')
                
                if not os.path.isfile(self.config):
                    # Running without configuration file
                    self.config = None
                    
                    print('Configuration file "config.py" not found on current directory!')
                    print('Loading slides without custom configurations...')
            else:
                raise NotADirectoryError('your media path {0} is not a valid directory'.format(self.media))
        else:
             raise NotADirectoryError('your presentation path {0} is not a valid directory'.format(self.path))

    def run(self, args=None):
        self.parse_args(args)

        app = FlaskReveal('flask_reveal')
        
        app.start(self.path, media_root=self.media, config=self.config, debug=self.debug)


command = Start()
