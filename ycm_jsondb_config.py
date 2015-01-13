def GetAdditionalFlags():
  flags = []

  # Xcode 5.1
  #flags.append('-isystem')
  #flags.append('/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../lib/c++/v1')
  #flags.append('-isystem')
  #flags.append('/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include')
  #flags.append('-isystem')
  #flags.append('/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../lib/clang/5.1/include')

  # Xcode 6
  #flags.append('-isystem')
  #flags.append('/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1')
  #flags.append('-isystem')
  #flags.append('/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include')
  #flags.append('-isystem')
  #flags.append('/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../lib/clang/6.0/include')

  # libc
  flags.append('-isystem')
  flags.append('/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.10.sdk/usr/include')

  # llvm+clang from source
  flags.append('-isystem')
  flags.append('/Users/mg/local/clang_src/llvm_installed/bin/../include/c++/v1')
  flags.append('-isystem')
  flags.append('/Users/mg/local/clang_src/llvm_installed/bin/../lib/clang/3.6.0/include')
  return flags
