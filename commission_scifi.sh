#!/bin/bash

for layer in {5..1}; do
    for module in {1..3}; do
        echo "Executing: ./set-channel-lv.py on scifi_${layer}x${module}"
        ./set-channel-lv.py on scifi_${layer}y${module}
        echo "Press Enter to continue..."
        read  # Wait for Enter key press
        ./set-channel-lv.py off scifi_${layer}y${module}
    done
done

