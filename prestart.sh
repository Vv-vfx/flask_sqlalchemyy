#!/bin/bash

flask db upgrade
flask main fill-db-fakes