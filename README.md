# flask-mini-apps-raspberrypi

Small self-hosted Flask apps on Raspberry Pi with SQLite, Nginx reverse proxy, systemd services, and deployment troubleshooting notes.

## Overview

This repository documents a small collection of self-hosted Flask applications deployed on a Raspberry Pi.

The project began as a simple book tracker and later expanded into a food tracker with notes for recipes and preparation steps. The main value of the project is not only the application code itself, but also the full deployment path: virtual environment setup, SQLite storage, Nginx reverse proxying, systemd services, and practical troubleshooting.

## Included Apps

### Book Tracker

* add books with title, author, and reading date
* edit existing entries
* delete entries
* simple browser-based list view

### Food Tracker

* add food entries
* store notes such as recipe details or preparation instructions
* edit existing entries
* delete entries
* simple browser-based list view

## Stack

* Raspberry Pi
* Python / Flask
* SQLite
* Nginx
* systemd
* Python virtual environment

## Goals

* build lightweight self-hosted tools for personal use
* deploy Flask applications in a practical Linux environment
* document a reusable Raspberry Pi deployment pattern
* capture troubleshooting lessons from a real setup process
* publish a cleaned public version of a real-world project

## Notes

This repository is based on a real Raspberry Pi setup adapted into a public example.

AI tools (ChatGPT) were used for ideation, debugging support, and documentation refinement. The final applications and deployment steps were tested manually in a real environment.

Sensitive information such as real domains, usernames, internal paths, and network details has been removed or generalized.
