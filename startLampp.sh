#!/bin/bash

sudo service apache2 stop
sudo service mysql stop
sudo /opt/lampp/lampp start
google-chrome http://localhost/bnn/dsp.php
