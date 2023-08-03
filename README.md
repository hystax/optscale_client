# OptScale Client
## *The OptScale Client tool by Hystax*

OptScale is a tool that helps you to integrate [OptScale](https://my.optscale.com/) components.

Components:




Basic usage:
```python
from optscale_client import Client

arcee = Client("arcee",  address="127.0.0.1", port="80",token='ffffff20-aaaa-4f7b-942a-7070711faf',
                secret='d0d006a9-ffff-450f-aaaa-bbfb9454bbba', verify=False)
print(arcee.runs_by_executor("XXXX"))
```