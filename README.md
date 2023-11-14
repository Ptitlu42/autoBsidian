## AUTOBSIDIAN

This Python script facilitates automatic synchronization between two instances of Obsidian, one at your workplace and one on your laptop. It uses Git to detect changes and automatically performs pull or push operations based on the detected differences.

**Requirements**

- Python 3.x installed on both machines
- Access to a Git service (GitHub, GitLab, Bitbucket, etc.)
- Write access to the local and remote Obsidian directories

**Installation**

- Clone this repository on both machines:

```bash

git clone https://github.com/
```

**Install dependencies:**

```bash

pip install -r requirements.txt
```

**Configuration**

- Configure Git information (username, email, etc.) on both machines:

```bash

git config --global user.name "Your Name"
```

```bash

git config --global user.email "your@email.com"
```

- copy the *.env.sample* file to *.env* and with the local and remote paths of Obsidian, as well as the URL of the remote repository.

```env

LOCAL_PATH=/path/to/obsidian/local
REMOTE_PATH=/path/to/obsidian/remote
REMOTE_URL=https://github.com/your-username/obsidian-notes.git
SYNC_INTERVAL=300  

```

**Usage**

- Run the script on both machines:

```bash

python obsidian_sync.py
```

The script will automatically compare local and remote Obsidian folders at the interval specified in config.json. If changes are detected, it will perform a pull or push accordingly.
