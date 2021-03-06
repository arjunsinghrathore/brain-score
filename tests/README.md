# Unit Tests
## Precomputed files
Some files have been pre-computed, but are too large to add to git.
They are automatically downloaded by executing `bash download_test_files.sh`.

## Markers
Unit tests have various markers that denote possible issues in the travis build:

* **private_access**: tests that require access to a private ressource, such as assemblies on S3 (travis pull request builds can not have private access)
* **memory_intense**: tests requiring more memory than is available in the travis sandbox (currently 3 GB, https://docs.travis-ci.com/user/common-build-problems/#my-build-script-is-killed-without-any-error)
* **requires_gpu**: tests requiring a GPU to run or to run in a reasonable time (travis does not support GPUs/CUDA)

Use the following syntax to mark a test:
```
@pytest.mark.memory_intense
def test_something(...):
    assert False
```

To skip a specific marker, run e.g. `pytest -m "not memory_intense"`.
To skip multiple markers, run e.g. `pytest -m "not private_access and not memory_intense"`.
