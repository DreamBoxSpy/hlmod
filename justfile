build:
    cd hlmod-hl/build && make -j$(nproc)

run:
    PYTHONPATH=/home/nerd/code/hlmod/.venv hlmod-hl/build/bin/hl PatchMe.hl