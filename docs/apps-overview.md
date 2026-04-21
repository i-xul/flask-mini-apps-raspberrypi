# Apps Overview

## Overview

This document explains the purpose of the two Flask applications included in this repository and the reasoning behind their design.

## Book Tracker

The book tracker was created to maintain a personal list of books that have been read.

The main goals were:

* to have a simple and accessible reading log
* to be able to update the list immediately after finishing a book
* to access the data from anywhere without relying on local files or physical notes

This resulted in a lightweight web application that provides a clear overview of completed books and their details.

## Food Tracker

The food tracker was created as a personal “digital cookbook”.

The main goals were:

* to store food ideas, recipes, and notes in one place
* to avoid relying on physical cookbooks or scattered notes
* to access recipes from anywhere when needed

This application focuses on storing reusable data rather than completed entries, making it more of a reference tool.

## Differences Between the Applications

Although both applications are technically similar, their purposes are clearly different:

* the **book tracker** records completed actions (books that have been read)
* the **food tracker** stores reusable information (recipes and notes for future use)

Because of this, the data models and usage patterns differ even though the underlying implementation is similar.

## Why Two Separate Applications

The decision to build two separate applications instead of combining them into one was intentional.

Reasons include:

* clearer separation of concerns
* simpler application logic per project
* easier maintenance and debugging
* better alignment with how the data is used

Keeping the applications separate also made it easier to iterate on each one independently during development.

## Summary

These applications demonstrate how small, purpose-built tools can solve specific everyday problems.

Instead of building a complex system, the focus was on:

* simplicity
* usability
* accessibility
* and practical deployment in a self-hosted environment
