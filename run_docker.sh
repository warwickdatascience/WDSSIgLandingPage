#!/bin/bash

docker run -itd --rm --restart always -v ${PWD}:/app -v /app/node_modules -p 3001:3000 -e CHOKIDAR_USEPOLLING=true ig_landing_page 
