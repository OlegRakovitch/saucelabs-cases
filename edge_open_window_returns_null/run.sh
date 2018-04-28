#!/bin/bash

docker run -ti \
  -e "SAUCE_USERNAME=$SAUCE_USERNAME" \
  -e "SAUCE_ACCESS_KEY=$SAUCE_ACCESS_KEY" \
  geslot/saucelabs-cases-edge-open-window-returns-null
