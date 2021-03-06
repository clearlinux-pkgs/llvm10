#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA2C794A986419D8A (tstellar@redhat.com)
#
%define keepstatic 1
Name     : llvm10
Version  : 10.0.1
Release  : 2
URL      : https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/llvm-10.0.1.src.tar.xz
Source0  : https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/llvm-10.0.1.src.tar.xz
Source1  : https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/v10.0.0/SPIRV-10.0.0.tar.gz
Source2  : https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/clang-10.0.1.src.tar.xz
Source3  : https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/compiler-rt-10.0.1.src.tar.xz
Source4  : https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/llvm-10.0.1.src.tar.xz.sig
Summary  : Google microbenchmark framework
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT NCSA
Requires: llvm10-bin = %{version}-%{release}
Requires: llvm10-lib = %{version}-%{release}
Requires: llvm10-license = %{version}-%{release}
Requires: llvm10-extras = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : Z3-dev
BuildRequires : binutils-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : libffi-dev
BuildRequires : libstdc++-dev
BuildRequires : libxml2-dev
BuildRequires : llvm
BuildRequires : llvm-dev
BuildRequires : ncurses-dev
BuildRequires : python3-dev
BuildRequires : valgrind-dev
BuildRequires : zlib-dev
Patch1: python2-shebangs.patch
Patch2: llvm-0001-CMake-Split-static-library-exports-into-their-own-ex.patch
Patch3: llvm-0002-Improve-physical-core-count-detection.patch
Patch4: llvm-0003-Produce-a-normally-versioned-libLLVM.patch
Patch5: llvm-0004-Allow-one-more-FMA-fusion.patch
Patch6: llvm-0005-Build-tablegen-component-as-a-shared-library.patch
Patch7: clang-0001-Build-a-single-shared-libclang.patch
Patch8: clang-0002-Don-t-install-Clang-static-libraries.patch
Patch9: clang-0002-Detect-Clear-Linux-and-apply-Clear-s-default-linker-.patch
Patch10: clang-0003-Make-Clang-default-to-Westmere-on-Clear-Linux.patch
Patch11: clang-0004-Add-the-LLVM-major-version-number-to-the-Gold-LTO-pl.patch
Patch12: clang-0005-Add-a-couple-more-f-instructions-that-GCC-has-that-C.patch
Patch13: SPIRV-0001-Fix-building-in-tree-with-cmake-DLLVM_LINK_LLVM_DYLI.patch

%description
This directory contains a "bundle" for doing syntax highlighting of TableGen
files for the Microsoft VSCode editor. The highlighting follows that done by
the TextMate "C" bundle as it is a translation of the textmate bundle to VSCode
using the "yo code" npm package. Currently, keywords, comments, and strings are
highlighted.

%package bin
Summary: bin components for the llvm10 package.
Group: Binaries
Requires: llvm10-license = %{version}-%{release}

%description bin
bin components for the llvm10 package.


%package dev
Summary: dev components for the llvm10 package.
Group: Development
Requires: llvm10-lib = %{version}-%{release}
Requires: llvm10-bin = %{version}-%{release}
Provides: llvm10-devel = %{version}-%{release}
Requires: llvm10 = %{version}-%{release}

%description dev
dev components for the llvm10 package.


%package extras
Summary: extras components for the llvm10 package.
Group: Default

%description extras
extras components for the llvm10 package.


%package extras-libllvm
Summary: extras-libllvm components for the llvm10 package.
Group: Default

%description extras-libllvm
extras-libllvm components for the llvm10 package.


%package lib
Summary: lib components for the llvm10 package.
Group: Libraries
Requires: llvm10-license = %{version}-%{release}

%description lib
lib components for the llvm10 package.


%package license
Summary: license components for the llvm10 package.
Group: Default

%description license
license components for the llvm10 package.


%prep
%setup -q -n llvm-10.0.1.src
cd %{_builddir}
tar xf %{_sourcedir}/clang-10.0.1.src.tar.xz
cd %{_builddir}
tar xf %{_sourcedir}/compiler-rt-10.0.1.src.tar.xz
cd %{_builddir}
tar xf %{_sourcedir}/SPIRV-10.0.0.tar.gz
cd %{_builddir}/llvm-10.0.1.src
mkdir -p tools/clang
cp -r %{_builddir}/clang-10.0.1.src/* %{_builddir}/llvm-10.0.1.src/tools/clang
mkdir -p projects/compiler-rt
cp -r %{_builddir}/compiler-rt-10.0.1.src/* %{_builddir}/llvm-10.0.1.src/projects/compiler-rt
mkdir -p projects/SPIRV
cp -r %{_builddir}/SPIRV-LLVM-Translator-10.0.0/* %{_builddir}/llvm-10.0.1.src/projects/SPIRV
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
## build_prepend content
# Bootstrap the table generators
# See https://build.opensuse.org/package/view_file/devel:tools:compiler/llvm10/llvm10.spec?expand=1
mkdir clr-bootstrap-build
pushd clr-bootstrap-build
CFLAGS="`sed -E 's/-Wl,\S+\s//g; s/-Wp,-D_FORTIFY_SOURCE=2//' <<<$CFLAGS` -fno-integrated-as"
CXXFLAGS="`sed -E 's/-Wl,\S+\s//g; s/-Wp,-D_FORTIFY_SOURCE=2//' <<<$CXXFLAGS` -fno-integrated-as"
%cmake .. \
-DCMAKE_BUILD_TYPE=Release \
-DBUILD_SHARED_LIBS:BOOL=OFF \
-DCMAKE_C_COMPILER=clang \
-DCMAKE_C_FLAGS="$CFLAGS -g0" \
-DCMAKE_CXX_COMPILER=clang++ \
-DCMAKE_CXX_FLAGS="$CXXFLAGS -g0" \
-DLLVM_BUILD_LLVM_DYLIB:BOOL=OFF \
-DLLVM_LINK_LLVM_DYLIB:BOOL=OFF \
-DLLVM_BUILD_TOOLS:BOOL=OFF \
-DLLVM_BUILD_UTILS:BOOL=OFF \
-DLLVM_BUILD_EXAMPLES:BOOL=OFF \
-DLLVM_POLLY_BUILD:BOOL=OFF \
-DLLVM_TOOL_CLANG_TOOLS_EXTRA_BUILD:BOOL=OFF \
-DLLVM_INCLUDE_TESTS:BOOL=OFF \
-DLLVM_ENABLE_ASSERTIONS=OFF \
-DLLVM_TARGETS_TO_BUILD=Native \
-DCLANG_ENABLE_ARCMT:BOOL=OFF \
-DCLANG_ENABLE_STATIC_ANALYZER:BOOL=OFF \
-DCOMPILER_RT_BUILD_SANITIZERS:BOOL=OFF \
-DCOMPILER_RT_BUILD_XRAY:BOOL=OFF \
-DLLDB_DISABLE_PYTHON=ON \
-DCMAKE_SKIP_RPATH:BOOL=OFF \
-DLLVM_LIBDIR_SUFFIX=64 \
-DLLVM_BINUTILS_INCDIR=/usr/include \
-DLLVM_HOST_TRIPLE="x86_64-generic-linux" \
-DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3
make  %{?_smp_mflags}  VERBOSE=1 llvm-tblgen clang-tblgen
popd

#export PATH=/usr/lib64/ccache/bin/:${PWD}/clr-bootstrap-build/bin:${PATH}
#export CC=${PWD}/clr-bootstrap-build/bin/clang
#export CXX=${PWD}/clr-bootstrap-build/bin/clang++
#export LLVM_AR=${PWD}/clr-bootstrap-build/bin/llvm-ar
#export LLVM_RANLIB=${PWD}/clr-bootstrap-build/bin/llvm-ranlib
export LLVM_TABLEGEN=${PWD}/clr-bootstrap-build/bin/llvm-tblgen
export CLANG_TABLEGEN=${PWD}/clr-bootstrap-build/bin/clang-tblgen
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618878181
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CFLAGS=${CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CXXFLAGS=${CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export FCFLAGS=$FFLAGS
unset LDFLAGS
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DCMAKE_C_FLAGS="`sed -E 's/-Wl,\S+\s//g; s/-Wp,-D_FORTIFY_SOURCE=2//' <<<$CFLAGS`" \
-DCMAKE_CXX_FLAGS="`sed -E 's/-Wl,\S+\s//g; s/-Wp,-D_FORTIFY_SOURCE=2//' <<<$CXXFLAGS`" \
-DCMAKE_EXE_LINKER_FLAGS="$CXXFLAGS -Wl,--as-needed -Wl,--build-id=sha1" \
-DCMAKE_MODULE_LINKER_FLAGS="$CXXFLAGS -Wl,--as-needed -Wl,--build-id=sha1" \
-DCMAKE_SHARED_LINKER_FLAGS="$CXXFLAGS -Wl,--as-needed -Wl,--build-id=sha1" \
-DENABLE_LINKER_BUILD_ID=ON \
-DBUILD_SHARED_LIBS:BOOL=OFF \
-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
-DCLANG_BUILD_SHARED_LIBS:BOOL=OFF \
-DLLVM_BUILD_RUNTIME:BOOL=ON \
-DLLVM_BUILD_TOOLS:BOOL=ON \
-DLLVM_ENABLE_CXX1Y=ON \
-DLLVM_ENABLE_FFI:BOOL=ON -DFFI_INCLUDE_DIR=`pkg-config --variable=includedir libffi` \
-DLLVM_ENABLE_LIBCXX:BOOL=OFF \
-DLLVM_ENABLE_RTTI:BOOL=ON \
-DLLVM_ENABLE_ZLIB:BOOL=ON \
-DLLVM_INSTALL_UTILS:BOOL=OFF \
-DLLVM_REQUIRES_RTTI:BOOL=ON \
-DLLVM_TABLEGEN=$LLVM_TABLEGEN \
-DCLANG_TABLEGEN=$CLANG_TABLEGEN \
-DLLVM_LIBDIR_SUFFIX=64 \
-DLLVM_BINUTILS_INCDIR=/usr/include \
-DLLVM_HOST_TRIPLE="x86_64-generic-linux" \
-DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3 \
-DCLANG_TOOL_SCAN_VIEW_BUILD:BOOL=OFF \
-DCLANG_TOOL_SCAN_BUILD_BUILD:BOOL=OFF \
-DLLVM_TOOL_OPT_VIEWER_BUILD:BOOL=OFF \
-DLLVM_INSTALL_UTILS:BOOL=OFF \
-DCMAKE_C_COMPILER=clang-11 \
-DCMAKE_CXX_COMPILER=clang++-11
make  %{?_smp_mflags}  VERBOSE=1
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test

%install
export SOURCE_DATE_EPOCH=1618878181
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/llvm10
cp %{_builddir}/SPIRV-LLVM-Translator-10.0.0/LICENSE.TXT %{buildroot}/usr/share/package-licenses/llvm10/8f178caf2a2d6e6c711a30da69077572df356cf6
cp %{_builddir}/clang-10.0.1.src/LICENSE.TXT %{buildroot}/usr/share/package-licenses/llvm10/a1691103171dc1d21cfa85f1d4809a16b9f1367f
cp %{_builddir}/clang-10.0.1.src/tools/clang-format-vs/ClangFormat/license.txt %{buildroot}/usr/share/package-licenses/llvm10/b5d4ab4d1191e592c03310adfbe90d99a46bf9d7
cp %{_builddir}/compiler-rt-10.0.1.src/LICENSE.TXT %{buildroot}/usr/share/package-licenses/llvm10/f4359b9da55a3b9e4d9513eb79cacf125fb49e7b
cp %{_builddir}/llvm-10.0.1.src/LICENSE.TXT %{buildroot}/usr/share/package-licenses/llvm10/af07f365643f841c69797e9059b66f0bd847f1cd
cp %{_builddir}/llvm-10.0.1.src/test/YAMLParser/LICENSE.txt %{buildroot}/usr/share/package-licenses/llvm10/c01c212bdf3925189f673e2081b44094023860ea
cp %{_builddir}/llvm-10.0.1.src/tools/msbuild/license.txt %{buildroot}/usr/share/package-licenses/llvm10/b5d4ab4d1191e592c03310adfbe90d99a46bf9d7
cp %{_builddir}/llvm-10.0.1.src/utils/benchmark/LICENSE %{buildroot}/usr/share/package-licenses/llvm10/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/llvm-10.0.1.src/utils/unittest/googlemock/LICENSE.txt %{buildroot}/usr/share/package-licenses/llvm10/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/llvm-10.0.1.src/utils/unittest/googletest/LICENSE.TXT %{buildroot}/usr/share/package-licenses/llvm10/5a2314153eadadc69258a9429104cd11804ea304
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/lib64/libgomp.so
rm -f %{buildroot}/usr/lib64/TestPlugin.so
rm -f %{buildroot}/usr/lib64/cmake/llvm/LLVMStaticExports.cmake
rm -f %{buildroot}/usr/lib64/cmake/llvm/LLVMStaticExports-relwithdebinfo.cmake
rm -f %{buildroot}/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.asan-i386.so
rm -f %{buildroot}/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.scudo-i386.so
rm -f %{buildroot}/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.scudo_minimal-i386.so
rm -f %{buildroot}/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.ubsan_minimal-i386.so
rm -f %{buildroot}/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.ubsan_standalone-i386.so
## install_append content
# Rename the Gold plugin elsewhere, as we're erasing *.so below
mv %{buildroot}/usr/lib64/LLVMgold.so %{buildroot}/usr/lib64/LLVMgold.so.save

# Remove files that should come from the main llvm package
rm -rf %{buildroot}/usr/include
rm -rf %{buildroot}/usr/lib64/*.a
rm -rf %{buildroot}/usr/lib64/*.so
rm -rf %{buildroot}/usr/lib64/cmake
rm -rf %{buildroot}/usr/lib64/pkgconfig
rm -rf %{buildroot}/usr/libexec

mv %{buildroot}/usr/share/package-licenses %{buildroot}/usr/
rm -rf %{buildroot}/usr/share/*
mv %{buildroot}/usr/package-licenses %{buildroot}/usr/share

# Move the tools to a versioned bin dir and then create symlinks back
pushd %{buildroot}/usr
FULL_VERSION=%{version}
VERSION=${FULL_VERSION%%%%.*}
mkdir -p lib64/clang/$FULL_VERSION/bin
mv bin/* lib64/clang/$FULL_VERSION/bin
for f in lib64/clang/$FULL_VERSION/bin/*; do
case "$f" in
*-$VERSION)
# Already versioned, leave it alone
continue
;;
esac
ln -s ../$f bin/${f##*/}-$VERSION
done

# libclang-cpp auto-relocates, so create a symlink so it finds its files
ln -s ../.. lib64/clang/$FULL_VERSION/lib64

# Put the LLVM gold plugin back, under the versioned name
mv lib64/LLVMgold.so.save lib64/LLVMgold-$VERSION.so
mkdir -p lib/bfd-plugins
ln -s ../../lib64/LLVMgold-$VERSION.so lib/bfd-plugins
popd
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/clang/10.0.1/bin/bugpoint
/usr/lib64/clang/10.0.1/bin/c-index-test
/usr/lib64/clang/10.0.1/bin/clang
/usr/lib64/clang/10.0.1/bin/clang++
/usr/lib64/clang/10.0.1/bin/clang-10
/usr/lib64/clang/10.0.1/bin/clang-check
/usr/lib64/clang/10.0.1/bin/clang-cl
/usr/lib64/clang/10.0.1/bin/clang-cpp
/usr/lib64/clang/10.0.1/bin/clang-extdef-mapping
/usr/lib64/clang/10.0.1/bin/clang-format
/usr/lib64/clang/10.0.1/bin/clang-import-test
/usr/lib64/clang/10.0.1/bin/clang-offload-bundler
/usr/lib64/clang/10.0.1/bin/clang-offload-wrapper
/usr/lib64/clang/10.0.1/bin/clang-refactor
/usr/lib64/clang/10.0.1/bin/clang-rename
/usr/lib64/clang/10.0.1/bin/clang-scan-deps
/usr/lib64/clang/10.0.1/bin/diagtool
/usr/lib64/clang/10.0.1/bin/dsymutil
/usr/lib64/clang/10.0.1/bin/git-clang-format
/usr/lib64/clang/10.0.1/bin/hmaptool
/usr/lib64/clang/10.0.1/bin/hwasan_symbolize
/usr/lib64/clang/10.0.1/bin/llc
/usr/lib64/clang/10.0.1/bin/lli
/usr/lib64/clang/10.0.1/bin/llvm-addr2line
/usr/lib64/clang/10.0.1/bin/llvm-ar
/usr/lib64/clang/10.0.1/bin/llvm-as
/usr/lib64/clang/10.0.1/bin/llvm-bcanalyzer
/usr/lib64/clang/10.0.1/bin/llvm-c-test
/usr/lib64/clang/10.0.1/bin/llvm-cat
/usr/lib64/clang/10.0.1/bin/llvm-cfi-verify
/usr/lib64/clang/10.0.1/bin/llvm-config
/usr/lib64/clang/10.0.1/bin/llvm-cov
/usr/lib64/clang/10.0.1/bin/llvm-cvtres
/usr/lib64/clang/10.0.1/bin/llvm-cxxdump
/usr/lib64/clang/10.0.1/bin/llvm-cxxfilt
/usr/lib64/clang/10.0.1/bin/llvm-cxxmap
/usr/lib64/clang/10.0.1/bin/llvm-diff
/usr/lib64/clang/10.0.1/bin/llvm-dis
/usr/lib64/clang/10.0.1/bin/llvm-dlltool
/usr/lib64/clang/10.0.1/bin/llvm-dwarfdump
/usr/lib64/clang/10.0.1/bin/llvm-dwp
/usr/lib64/clang/10.0.1/bin/llvm-elfabi
/usr/lib64/clang/10.0.1/bin/llvm-exegesis
/usr/lib64/clang/10.0.1/bin/llvm-extract
/usr/lib64/clang/10.0.1/bin/llvm-ifs
/usr/lib64/clang/10.0.1/bin/llvm-install-name-tool
/usr/lib64/clang/10.0.1/bin/llvm-jitlink
/usr/lib64/clang/10.0.1/bin/llvm-lib
/usr/lib64/clang/10.0.1/bin/llvm-link
/usr/lib64/clang/10.0.1/bin/llvm-lipo
/usr/lib64/clang/10.0.1/bin/llvm-lto
/usr/lib64/clang/10.0.1/bin/llvm-lto2
/usr/lib64/clang/10.0.1/bin/llvm-mc
/usr/lib64/clang/10.0.1/bin/llvm-mca
/usr/lib64/clang/10.0.1/bin/llvm-modextract
/usr/lib64/clang/10.0.1/bin/llvm-mt
/usr/lib64/clang/10.0.1/bin/llvm-nm
/usr/lib64/clang/10.0.1/bin/llvm-objcopy
/usr/lib64/clang/10.0.1/bin/llvm-objdump
/usr/lib64/clang/10.0.1/bin/llvm-opt-report
/usr/lib64/clang/10.0.1/bin/llvm-pdbutil
/usr/lib64/clang/10.0.1/bin/llvm-profdata
/usr/lib64/clang/10.0.1/bin/llvm-ranlib
/usr/lib64/clang/10.0.1/bin/llvm-rc
/usr/lib64/clang/10.0.1/bin/llvm-readelf
/usr/lib64/clang/10.0.1/bin/llvm-readobj
/usr/lib64/clang/10.0.1/bin/llvm-reduce
/usr/lib64/clang/10.0.1/bin/llvm-rtdyld
/usr/lib64/clang/10.0.1/bin/llvm-size
/usr/lib64/clang/10.0.1/bin/llvm-spirv
/usr/lib64/clang/10.0.1/bin/llvm-split
/usr/lib64/clang/10.0.1/bin/llvm-stress
/usr/lib64/clang/10.0.1/bin/llvm-strings
/usr/lib64/clang/10.0.1/bin/llvm-strip
/usr/lib64/clang/10.0.1/bin/llvm-symbolizer
/usr/lib64/clang/10.0.1/bin/llvm-tblgen
/usr/lib64/clang/10.0.1/bin/llvm-undname
/usr/lib64/clang/10.0.1/bin/llvm-xray
/usr/lib64/clang/10.0.1/bin/obj2yaml
/usr/lib64/clang/10.0.1/bin/opt
/usr/lib64/clang/10.0.1/bin/sancov
/usr/lib64/clang/10.0.1/bin/sanstats
/usr/lib64/clang/10.0.1/bin/verify-uselistorder
/usr/lib64/clang/10.0.1/bin/yaml2obj
/usr/lib64/clang/10.0.1/include/openmp_wrappers/cmath
/usr/lib64/clang/10.0.1/include/profile/InstrProfData.inc
/usr/lib64/clang/10.0.1/lib/linux/clang_rt.crtbegin-x86_64.o
/usr/lib64/clang/10.0.1/lib/linux/clang_rt.crtend-x86_64.o
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.asan-preinit-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.asan-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.asan-x86_64.a.syms
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.asan_cxx-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.asan_cxx-x86_64.a.syms
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.builtins-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.cfi-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.cfi_diag-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.dd-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.dfsan-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.dfsan-x86_64.a.syms
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.fuzzer-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.fuzzer_no_main-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.gwp_asan-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.hwasan-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.hwasan-x86_64.a.syms
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.hwasan_cxx-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.hwasan_cxx-x86_64.a.syms
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.lsan-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.msan-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.msan-x86_64.a.syms
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.msan_cxx-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.msan_cxx-x86_64.a.syms
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.profile-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.safestack-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.scudo-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.scudo_cxx-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.scudo_cxx_minimal-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.scudo_minimal-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.scudo_standalone-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.scudo_standalone_cxx-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.stats-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.stats_client-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.tsan-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.tsan-x86_64.a.syms
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.tsan_cxx-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.tsan_cxx-x86_64.a.syms
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.ubsan_minimal-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.ubsan_minimal-x86_64.a.syms
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.ubsan_standalone-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.ubsan_standalone-x86_64.a.syms
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.ubsan_standalone_cxx-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.ubsan_standalone_cxx-x86_64.a.syms
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.xray-basic-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.xray-fdr-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.xray-profiling-x86_64.a
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.xray-x86_64.a
/usr/lib64/clang/10.0.1/lib64
/usr/lib64/clang/10.0.1/share/asan_blacklist.txt
/usr/lib64/clang/10.0.1/share/cfi_blacklist.txt
/usr/lib64/clang/10.0.1/share/dfsan_abilist.txt
/usr/lib64/clang/10.0.1/share/hwasan_blacklist.txt
/usr/lib64/clang/10.0.1/share/msan_blacklist.txt

%files bin
%defattr(-,root,root,-)
/usr/bin/bugpoint-10
/usr/bin/c-index-test-10
/usr/bin/clang++-10
/usr/bin/clang-10
/usr/bin/clang-check-10
/usr/bin/clang-cl-10
/usr/bin/clang-cpp-10
/usr/bin/clang-extdef-mapping-10
/usr/bin/clang-format-10
/usr/bin/clang-import-test-10
/usr/bin/clang-offload-bundler-10
/usr/bin/clang-offload-wrapper-10
/usr/bin/clang-refactor-10
/usr/bin/clang-rename-10
/usr/bin/clang-scan-deps-10
/usr/bin/diagtool-10
/usr/bin/dsymutil-10
/usr/bin/git-clang-format-10
/usr/bin/hmaptool-10
/usr/bin/hwasan_symbolize-10
/usr/bin/llc-10
/usr/bin/lli-10
/usr/bin/llvm-addr2line-10
/usr/bin/llvm-ar-10
/usr/bin/llvm-as-10
/usr/bin/llvm-bcanalyzer-10
/usr/bin/llvm-c-test-10
/usr/bin/llvm-cat-10
/usr/bin/llvm-cfi-verify-10
/usr/bin/llvm-config-10
/usr/bin/llvm-cov-10
/usr/bin/llvm-cvtres-10
/usr/bin/llvm-cxxdump-10
/usr/bin/llvm-cxxfilt-10
/usr/bin/llvm-cxxmap-10
/usr/bin/llvm-diff-10
/usr/bin/llvm-dis-10
/usr/bin/llvm-dlltool-10
/usr/bin/llvm-dwarfdump-10
/usr/bin/llvm-dwp-10
/usr/bin/llvm-elfabi-10
/usr/bin/llvm-exegesis-10
/usr/bin/llvm-extract-10
/usr/bin/llvm-ifs-10
/usr/bin/llvm-install-name-tool-10
/usr/bin/llvm-jitlink-10
/usr/bin/llvm-lib-10
/usr/bin/llvm-link-10
/usr/bin/llvm-lipo-10
/usr/bin/llvm-lto-10
/usr/bin/llvm-lto2-10
/usr/bin/llvm-mc-10
/usr/bin/llvm-mca-10
/usr/bin/llvm-modextract-10
/usr/bin/llvm-mt-10
/usr/bin/llvm-nm-10
/usr/bin/llvm-objcopy-10
/usr/bin/llvm-objdump-10
/usr/bin/llvm-opt-report-10
/usr/bin/llvm-pdbutil-10
/usr/bin/llvm-profdata-10
/usr/bin/llvm-ranlib-10
/usr/bin/llvm-rc-10
/usr/bin/llvm-readelf-10
/usr/bin/llvm-readobj-10
/usr/bin/llvm-reduce-10
/usr/bin/llvm-rtdyld-10
/usr/bin/llvm-size-10
/usr/bin/llvm-spirv-10
/usr/bin/llvm-split-10
/usr/bin/llvm-stress-10
/usr/bin/llvm-strings-10
/usr/bin/llvm-strip-10
/usr/bin/llvm-symbolizer-10
/usr/bin/llvm-tblgen-10
/usr/bin/llvm-undname-10
/usr/bin/llvm-xray-10
/usr/bin/obj2yaml-10
/usr/bin/opt-10
/usr/bin/sancov-10
/usr/bin/sanstats-10
/usr/bin/verify-uselistorder-10
/usr/bin/yaml2obj-10

%files dev
%defattr(-,root,root,-)
/usr/lib64/clang/10.0.1/include/arm_cmse.h
/usr/lib64/clang/10.0.1/include/arm_mve.h
/usr/lib64/clang/10.0.1/include/fuzzer/FuzzedDataProvider.h
/usr/lib64/clang/10.0.1/include/ppc_wrappers/pmmintrin.h
/usr/lib64/clang/10.0.1/include/ppc_wrappers/smmintrin.h
/usr/lib64/clang/10.0.1/include/ppc_wrappers/tmmintrin.h
/usr/lib64/clang/10.0.1/include/sanitizer/ubsan_interface.h

%files extras
%defattr(-,root,root,-)
/usr/lib64/LLVMgold-10.so
/usr/lib64/clang/10.0.1/include/__clang_cuda_builtin_vars.h
/usr/lib64/clang/10.0.1/include/__clang_cuda_cmath.h
/usr/lib64/clang/10.0.1/include/__clang_cuda_complex_builtins.h
/usr/lib64/clang/10.0.1/include/__clang_cuda_device_functions.h
/usr/lib64/clang/10.0.1/include/__clang_cuda_intrinsics.h
/usr/lib64/clang/10.0.1/include/__clang_cuda_libdevice_declares.h
/usr/lib64/clang/10.0.1/include/__clang_cuda_math_forward_declares.h
/usr/lib64/clang/10.0.1/include/__clang_cuda_runtime_wrapper.h
/usr/lib64/clang/10.0.1/include/__stddef_max_align_t.h
/usr/lib64/clang/10.0.1/include/__wmmintrin_aes.h
/usr/lib64/clang/10.0.1/include/__wmmintrin_pclmul.h
/usr/lib64/clang/10.0.1/include/adxintrin.h
/usr/lib64/clang/10.0.1/include/altivec.h
/usr/lib64/clang/10.0.1/include/ammintrin.h
/usr/lib64/clang/10.0.1/include/arm64intr.h
/usr/lib64/clang/10.0.1/include/arm_acle.h
/usr/lib64/clang/10.0.1/include/arm_fp16.h
/usr/lib64/clang/10.0.1/include/arm_neon.h
/usr/lib64/clang/10.0.1/include/armintr.h
/usr/lib64/clang/10.0.1/include/avx2intrin.h
/usr/lib64/clang/10.0.1/include/avx512bf16intrin.h
/usr/lib64/clang/10.0.1/include/avx512bitalgintrin.h
/usr/lib64/clang/10.0.1/include/avx512bwintrin.h
/usr/lib64/clang/10.0.1/include/avx512cdintrin.h
/usr/lib64/clang/10.0.1/include/avx512dqintrin.h
/usr/lib64/clang/10.0.1/include/avx512erintrin.h
/usr/lib64/clang/10.0.1/include/avx512fintrin.h
/usr/lib64/clang/10.0.1/include/avx512ifmaintrin.h
/usr/lib64/clang/10.0.1/include/avx512ifmavlintrin.h
/usr/lib64/clang/10.0.1/include/avx512pfintrin.h
/usr/lib64/clang/10.0.1/include/avx512vbmi2intrin.h
/usr/lib64/clang/10.0.1/include/avx512vbmiintrin.h
/usr/lib64/clang/10.0.1/include/avx512vbmivlintrin.h
/usr/lib64/clang/10.0.1/include/avx512vlbf16intrin.h
/usr/lib64/clang/10.0.1/include/avx512vlbitalgintrin.h
/usr/lib64/clang/10.0.1/include/avx512vlbwintrin.h
/usr/lib64/clang/10.0.1/include/avx512vlcdintrin.h
/usr/lib64/clang/10.0.1/include/avx512vldqintrin.h
/usr/lib64/clang/10.0.1/include/avx512vlintrin.h
/usr/lib64/clang/10.0.1/include/avx512vlvbmi2intrin.h
/usr/lib64/clang/10.0.1/include/avx512vlvnniintrin.h
/usr/lib64/clang/10.0.1/include/avx512vlvp2intersectintrin.h
/usr/lib64/clang/10.0.1/include/avx512vnniintrin.h
/usr/lib64/clang/10.0.1/include/avx512vp2intersectintrin.h
/usr/lib64/clang/10.0.1/include/avx512vpopcntdqintrin.h
/usr/lib64/clang/10.0.1/include/avx512vpopcntdqvlintrin.h
/usr/lib64/clang/10.0.1/include/avxintrin.h
/usr/lib64/clang/10.0.1/include/bmi2intrin.h
/usr/lib64/clang/10.0.1/include/bmiintrin.h
/usr/lib64/clang/10.0.1/include/cetintrin.h
/usr/lib64/clang/10.0.1/include/cldemoteintrin.h
/usr/lib64/clang/10.0.1/include/clflushoptintrin.h
/usr/lib64/clang/10.0.1/include/clwbintrin.h
/usr/lib64/clang/10.0.1/include/clzerointrin.h
/usr/lib64/clang/10.0.1/include/cpuid.h
/usr/lib64/clang/10.0.1/include/cuda_wrappers/algorithm
/usr/lib64/clang/10.0.1/include/cuda_wrappers/complex
/usr/lib64/clang/10.0.1/include/cuda_wrappers/new
/usr/lib64/clang/10.0.1/include/emmintrin.h
/usr/lib64/clang/10.0.1/include/enqcmdintrin.h
/usr/lib64/clang/10.0.1/include/f16cintrin.h
/usr/lib64/clang/10.0.1/include/float.h
/usr/lib64/clang/10.0.1/include/fma4intrin.h
/usr/lib64/clang/10.0.1/include/fmaintrin.h
/usr/lib64/clang/10.0.1/include/fxsrintrin.h
/usr/lib64/clang/10.0.1/include/gfniintrin.h
/usr/lib64/clang/10.0.1/include/htmintrin.h
/usr/lib64/clang/10.0.1/include/htmxlintrin.h
/usr/lib64/clang/10.0.1/include/ia32intrin.h
/usr/lib64/clang/10.0.1/include/immintrin.h
/usr/lib64/clang/10.0.1/include/intrin.h
/usr/lib64/clang/10.0.1/include/inttypes.h
/usr/lib64/clang/10.0.1/include/invpcidintrin.h
/usr/lib64/clang/10.0.1/include/iso646.h
/usr/lib64/clang/10.0.1/include/limits.h
/usr/lib64/clang/10.0.1/include/lwpintrin.h
/usr/lib64/clang/10.0.1/include/lzcntintrin.h
/usr/lib64/clang/10.0.1/include/mm3dnow.h
/usr/lib64/clang/10.0.1/include/mm_malloc.h
/usr/lib64/clang/10.0.1/include/mmintrin.h
/usr/lib64/clang/10.0.1/include/module.modulemap
/usr/lib64/clang/10.0.1/include/movdirintrin.h
/usr/lib64/clang/10.0.1/include/msa.h
/usr/lib64/clang/10.0.1/include/mwaitxintrin.h
/usr/lib64/clang/10.0.1/include/nmmintrin.h
/usr/lib64/clang/10.0.1/include/opencl-c-base.h
/usr/lib64/clang/10.0.1/include/opencl-c.h
/usr/lib64/clang/10.0.1/include/openmp_wrappers/__clang_openmp_math.h
/usr/lib64/clang/10.0.1/include/openmp_wrappers/__clang_openmp_math_declares.h
/usr/lib64/clang/10.0.1/include/openmp_wrappers/math.h
/usr/lib64/clang/10.0.1/include/pconfigintrin.h
/usr/lib64/clang/10.0.1/include/pkuintrin.h
/usr/lib64/clang/10.0.1/include/pmmintrin.h
/usr/lib64/clang/10.0.1/include/popcntintrin.h
/usr/lib64/clang/10.0.1/include/ppc_wrappers/emmintrin.h
/usr/lib64/clang/10.0.1/include/ppc_wrappers/mm_malloc.h
/usr/lib64/clang/10.0.1/include/ppc_wrappers/mmintrin.h
/usr/lib64/clang/10.0.1/include/ppc_wrappers/xmmintrin.h
/usr/lib64/clang/10.0.1/include/prfchwintrin.h
/usr/lib64/clang/10.0.1/include/ptwriteintrin.h
/usr/lib64/clang/10.0.1/include/rdseedintrin.h
/usr/lib64/clang/10.0.1/include/rtmintrin.h
/usr/lib64/clang/10.0.1/include/s390intrin.h
/usr/lib64/clang/10.0.1/include/sanitizer/allocator_interface.h
/usr/lib64/clang/10.0.1/include/sanitizer/asan_interface.h
/usr/lib64/clang/10.0.1/include/sanitizer/common_interface_defs.h
/usr/lib64/clang/10.0.1/include/sanitizer/coverage_interface.h
/usr/lib64/clang/10.0.1/include/sanitizer/dfsan_interface.h
/usr/lib64/clang/10.0.1/include/sanitizer/hwasan_interface.h
/usr/lib64/clang/10.0.1/include/sanitizer/linux_syscall_hooks.h
/usr/lib64/clang/10.0.1/include/sanitizer/lsan_interface.h
/usr/lib64/clang/10.0.1/include/sanitizer/msan_interface.h
/usr/lib64/clang/10.0.1/include/sanitizer/netbsd_syscall_hooks.h
/usr/lib64/clang/10.0.1/include/sanitizer/scudo_interface.h
/usr/lib64/clang/10.0.1/include/sanitizer/tsan_interface.h
/usr/lib64/clang/10.0.1/include/sanitizer/tsan_interface_atomic.h
/usr/lib64/clang/10.0.1/include/sgxintrin.h
/usr/lib64/clang/10.0.1/include/shaintrin.h
/usr/lib64/clang/10.0.1/include/smmintrin.h
/usr/lib64/clang/10.0.1/include/stdalign.h
/usr/lib64/clang/10.0.1/include/stdarg.h
/usr/lib64/clang/10.0.1/include/stdatomic.h
/usr/lib64/clang/10.0.1/include/stdbool.h
/usr/lib64/clang/10.0.1/include/stddef.h
/usr/lib64/clang/10.0.1/include/stdint.h
/usr/lib64/clang/10.0.1/include/stdnoreturn.h
/usr/lib64/clang/10.0.1/include/tbmintrin.h
/usr/lib64/clang/10.0.1/include/tgmath.h
/usr/lib64/clang/10.0.1/include/tmmintrin.h
/usr/lib64/clang/10.0.1/include/unwind.h
/usr/lib64/clang/10.0.1/include/vadefs.h
/usr/lib64/clang/10.0.1/include/vaesintrin.h
/usr/lib64/clang/10.0.1/include/varargs.h
/usr/lib64/clang/10.0.1/include/vecintrin.h
/usr/lib64/clang/10.0.1/include/vpclmulqdqintrin.h
/usr/lib64/clang/10.0.1/include/waitpkgintrin.h
/usr/lib64/clang/10.0.1/include/wbnoinvdintrin.h
/usr/lib64/clang/10.0.1/include/wmmintrin.h
/usr/lib64/clang/10.0.1/include/x86intrin.h
/usr/lib64/clang/10.0.1/include/xmmintrin.h
/usr/lib64/clang/10.0.1/include/xopintrin.h
/usr/lib64/clang/10.0.1/include/xray/xray_interface.h
/usr/lib64/clang/10.0.1/include/xray/xray_log_interface.h
/usr/lib64/clang/10.0.1/include/xray/xray_records.h
/usr/lib64/clang/10.0.1/include/xsavecintrin.h
/usr/lib64/clang/10.0.1/include/xsaveintrin.h
/usr/lib64/clang/10.0.1/include/xsaveoptintrin.h
/usr/lib64/clang/10.0.1/include/xsavesintrin.h
/usr/lib64/clang/10.0.1/include/xtestintrin.h
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.asan-x86_64.so
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.dyndd-x86_64.so
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.hwasan-x86_64.so
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.scudo-x86_64.so
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.scudo_minimal-x86_64.so
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.ubsan_minimal-x86_64.so
/usr/lib64/clang/10.0.1/lib/linux/libclang_rt.ubsan_standalone-x86_64.so

%files extras-libllvm
%defattr(-,root,root,-)
/usr/lib64/libLLVM.so.10

%files lib
%defattr(-,root,root,-)
/usr/lib/bfd-plugins/LLVMgold-10.so
/usr/lib64/libLLVMTableGen.so.10
/usr/lib64/libLTO.so.10
/usr/lib64/libRemarks.so.10
/usr/lib64/libclang-cpp.so.10
/usr/lib64/libclang.so.10

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/llvm10/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/llvm10/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/llvm10/8f178caf2a2d6e6c711a30da69077572df356cf6
/usr/share/package-licenses/llvm10/a1691103171dc1d21cfa85f1d4809a16b9f1367f
/usr/share/package-licenses/llvm10/af07f365643f841c69797e9059b66f0bd847f1cd
/usr/share/package-licenses/llvm10/b5d4ab4d1191e592c03310adfbe90d99a46bf9d7
/usr/share/package-licenses/llvm10/c01c212bdf3925189f673e2081b44094023860ea
/usr/share/package-licenses/llvm10/f4359b9da55a3b9e4d9513eb79cacf125fb49e7b
