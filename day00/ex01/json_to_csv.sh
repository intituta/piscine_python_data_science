#!/bin/bash

jq '.items' ../ex00/hh.json | jq -r -f filter.jq > hh.csv