# Checkpoint-Firewall-IP-Address-Extractor
This script extracts IP addresses from group objects in Checkpoint Firewall configurations.
## Table of Contents
- Introduction
- Prerequisites
## Introduction
This repository contains a Python script that parses Checkpoint Firewall configurations to extract IP addresses from group objects. Group objects in Checkpoint Firewall often contain multiple IP addresses, making it useful to extract them for various operational tasks such as logging or analysis.
## Prerequisites
You need to get the output of Group object from Checkpoint Firewall using following command and save the json file where python script will run
  #### mgmt show group name 'GROUP_NAME' --format json
