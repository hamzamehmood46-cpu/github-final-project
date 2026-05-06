#!/bin/bash

echo "Simple Interest Calculator"
echo

read -p "Enter the principal amount: " principal
read -p "Enter the rate of interest: " rate
read -p "Enter the time period: " time

simple_interest=$((principal * rate * time / 100))

echo
echo "Simple Interest is: $simple_interest"
