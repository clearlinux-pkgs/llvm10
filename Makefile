PKG_NAME := llvm10
URL = https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/llvm-10.0.1.src.tar.xz
ARCHIVES = https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/clang-10.0.1.src.tar.xz tools/clang https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/compiler-rt-10.0.1.src.tar.xz projects/compiler-rt https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/v10.0.0/SPIRV-10.0.0.tar.gz projects/SPIRV

include ../common/Makefile.common
