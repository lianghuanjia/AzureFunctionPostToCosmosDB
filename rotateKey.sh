#!/bin/bash
brew update
brew upgrade
brew install azure-cli   
az login 
az account set --subscription <my subscription id>
az functionapp keys delete -g assignment4 -n functionsInPortal --key-type functionKeys --key-name key
az functionapp keys set -g assignment4 -n functionsInPortal --key-type functionKeys --key-name key