build:
    cd hlmod-hl/build && cmake --build . --parallel

prepare:
    rm -Rf hlmod-hl/build
    mkdir -p hlmod-hl/build
    cd hlmod-hl/build && cmake ..

# VS2022 Community: "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Auxiliary/Build/vcvarsall.bat"
# VS2019 Community: "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Auxiliary/Build/vcvarsall.bat"
MSVC_VARS_SCRIPT := "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Auxiliary/Build/vcvarsall.bat"

prepare-win:
    #!cmd.exe /C
    IF EXIST hlmod-hl\build rmdir /s /q hlmod-hl\build
    mkdir hlmod-hl\build
    cd hlmod-hl\build && "{{MSVC_VARS_SCRIPT}}" x64 && cmake -G "Ninja" .. -DCMAKE_TOOLCHAIN_FILE=D:/vcpkg/scripts/buildsystems/vcpkg.cmake -DVCPKG_TARGET_TRIPLET=x64-windows

build-win:
    #!cmd.exe /C
    cd hlmod-hl\build && "{{MSVC_VARS_SCRIPT}}" x64 && cmake --build . --parallel

run:
    PYTHONPATH=/home/nerd/code/hlmod/.venv hlmod-hl/build/bin/hl PatchMe.hl
