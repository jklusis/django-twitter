#!/usr/bin/env bash

ssh() {
    echo "Connecting to workspace.."
    docker-compose exec python /bin/sh
}

up() {
    echo "Bringing up docker containers.."
    docker-compose up -d
    echo "Done!"
}

down() {
    echo "Bringing down docker containers.."
    docker-compose down
    echo "Done!"
}

restart() {
    echo "Rebooting docker containers.."
    down
    up
}

if [[ -n "$1" ]]; then
    command="$1"
    if [[ -n "$(type -t "${command}")" ]] && [[ "$(type -t "${command}")" == function ]]; then
        "$command" "${@:2}"
        exit
    else
        echo "Command not found"
        exit
    fi
fi
