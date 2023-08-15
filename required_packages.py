"""Central place to hold the `setup.py` dependencies.
This way, the automation shell scripts can read them.
"""

REQUIRED_PACKAGES = [
    'numpy>=1.13.3',
    'jax[cuda]',
]

if __name__ == '__main__':
  # For using `pip` in shell scripts.
  print(' '.join(REQUIRED_PACKAGES))
