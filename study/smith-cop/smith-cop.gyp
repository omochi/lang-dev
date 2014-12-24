{
  'variables': {
  },
  'includes': [
  ],
  'target_defaults': {

  },
  'targets': [
    {
      'target_name': 'main',
      'type': 'executable',
      'dependencies': [
      ],
      'sources': [
        'src/main.cc'
      ],
      'include_dirs': [
        'include'
      ],
      'defines': [
      ],
      'xcode_settings': {
        'CLANG_CXX_LANGUAGE_STANDARD': 'gnu++11',
        'CLANG_CXX_LIBRARY': 'libc++',
        'WARNING_CFLAGS': ['-Wall']
      }
    },
  ],
}