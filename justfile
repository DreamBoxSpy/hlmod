build:
    cd hlmod-hl/build && cmake --build . --parallel

prepare:
    rm -Rf hlmod-hl/build
    mkdir -p hlmod-hl/build
    cd hlmod-hl/build && cmake ..

prepare-win:
    rm -Rf hlmod-hl/build
    mkdir -p hlmod-hl/build
    cd hlmod-hl/build && cmake .. -DCMAKE_TOOLCHAIN_FILE=D:/vcpkg/scripts/buildsystems/vcpkg.cmake \
                                  -DVCPKG_TARGET_TRIPLET=x64-windows

run:
    PYTHONPATH=/home/nerd/code/hlmod/.venv hlmod-hl/build/bin/hl PatchMe.hl
