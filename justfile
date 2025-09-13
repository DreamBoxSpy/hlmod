build:
    cd hlmod-hl/build && cmake --build . --parallel

prepare:
    rm -Rf hlmod-hl/build
    mkdir -p hlmod-hl/build
    cd hlmod-hl/build && cmake -G "Ninja" ..

# VS2022 Community: "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Auxiliary/Build/vcvarsall.bat"
# VS2019 Community: "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Auxiliary/Build/vcvarsall.bat"
MSVC_VARS_SCRIPT := "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Auxiliary/Build/vcvarsall.bat"

prepare-win:
    #!cmd.exe /C
    IF EXIST hlmod-hl\build rmdir /s /q hlmod-hl\build
    mkdir hlmod-hl\build
    cd hlmod-hl\build && "{{MSVC_VARS_SCRIPT}}" x64 && cmake -G "Ninja" .. -DCMAKE_TOOLCHAIN_FILE=D:/vcpkg/scripts/buildsystems/vcpkg.cmake -DVCPKG_TARGET_TRIPLET=x64-windows -DCMAKE_BUILD_TYPE=Release

build-win:
    #!cmd.exe /C
    cd hlmod-hl\build && "{{MSVC_VARS_SCRIPT}}" x64 && cmake --build . --parallel

run:
    PYTHONPATH=/home/nerd/code/hlmod/.venv hlmod-hl/build/bin/hl PatchMe.hl

run-win:
    #!cmd.exe /C
    hlmod-hl\build\bin\hl.exe PatchMe.hl

hlsteam:
    mkdir -p hlsteam/native/include/steam
    mkdir -p hlsteam/native/lib/win32
    mkdir -p hlsteam/native/lib/osx64
    mkdir -p hlsteam/native/lib/linux32
    mkdir -p hlsteam/native/lib/linux64
    cp ./Steamworks-SDK/public/steam/*.h hlsteam/native/include/steam
    cp ./Steamworks-SDK/redistributable_bin/steam_api.dll hlsteam/native/lib/win32 > /dev/null
    cp ./Steamworks-SDK/redistributable_bin/steam_api.lib hlsteam/native/lib/win32 > /dev/null
    cp ./Steamworks-SDK/redistributable_bin/osx/libsteam_api.dylib hlsteam/native/lib/osx64 > /dev/null
    cp ./Steamworks-SDK/redistributable_bin/linux32/libsteam_api.so hlsteam/native/lib/linux32 > /dev/null
    cp ./Steamworks-SDK/redistributable_bin/linux64/libsteam_api.so hlsteam/native/lib/linux64 > /dev/null
    cp ./hlmod-hl/src/hl.h hlsteam/native/include > /dev/null
    cd hlsteam && make
    cp hlsteam/steam.hdll hlmod-hl/build/bin/steam.hdll
    cp ./Steamworks-SDK/redistributable_bin/linux64/libsteam_api.so hlmod-hl/build/bin/libsteam_api.so

hlchroma:
    #!cmd.exe /C
    # windows only!
    rm -Rf hlchroma/build
    cd hlchroma && mkdir build && cd build && cmake -G "Ninja" .. && cmake --build . --parallel && cd ..\..\
    cp hlchroma\build\chroma.hdll hdll\

pull:
    cd hlmod-hl && proxychains git pull
    proxychains git pull

push:
    cd hlmod-hl && proxychains git push
    proxychains git push