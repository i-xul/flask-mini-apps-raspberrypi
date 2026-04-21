# Project Notes

## Purpose

This project started as a simple need for lightweight tools:

* tracking books
* tracking food entries and notes

Instead of using existing heavy solutions, the goal was to build small, self-hosted applications that are easy to deploy and maintain on a Raspberry Pi.

---

## What I learned

During this project I learned more about:

* building small Flask applications with SQLite
* structuring simple CRUD-style web apps
* using Python virtual environments in practice
* deploying Flask apps beyond development mode
* integrating Flask with Nginx via reverse proxy
* managing applications with systemd
* debugging real deployment issues

---

## Practical lessons

### Deployment is harder than coding

The application logic itself was relatively simple.

Most challenges came from:

* environment setup
* dependency issues
* service configuration
* reverse proxy routing

---

### Small mistakes break the whole system

Examples:

* missing Python modules
* incorrect service paths
* wrong port configuration
* mismatched Nginx routes

These issues required systematic debugging rather than guessing.

---

### Iteration improves understanding

The project evolved step by step:

1. initial book tracker
2. adding edit and delete functionality
3. building a second app (food tracker)
4. deploying behind Nginx
5. converting into systemd services

Each step added complexity and required adjustments.

---

### Lightweight tools can be enough

Instead of large frameworks or complex databases:

* Flask + SQLite provided everything needed
* simple HTML templates were sufficient
* the focus stayed on functionality and deployment

---

## Portfolio note

This repository represents a real Raspberry Pi project adapted into a public example.

Sensitive details such as usernames, domains, and internal paths have been removed.

AI tools were used during development for ideation, debugging support, and documentation, but all applications and deployment steps were tested manually.
