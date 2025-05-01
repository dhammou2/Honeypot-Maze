## Step 1: Create the Honeypot Base Folder

Create the root honeypot directory and its initial subfolder:

```bash
mkdir -p /home/dahammoudeh/SystemLogs/sys_1234
```

This folder will serve as the attacker’s entry point.

---

## Step 2: Create a Persistent Audit Rule

Create a rule file to monitor all activity inside `SystemLogs`.

```bash
sudo nano /etc/audit/rules.d/honeypot.rules
```

Paste the following rule:

```
-a always,exit -F dir=/home/dahammoudeh/SystemLogs -F perm=warx -k honeypot_activity
```

Save and exit the file.

---

## Step 3: Load the Audit Rule

Activate the rule so it applies immediately:

```bash
sudo augenrules --load
```

Verify it's working:

```bash
sudo auditctl -l
```

You should see the `honeypot_activity` rule listed.

---

## Step 4: Start the Watcher Script

This script monitors access to subfolders and triggers fake file and folder generation.

```bash
bash watcher.sh
```

---

## Step 5: Trigger the Honeypot

When an attacker enters a subfolder like `sys_1234`, the watcher script calls `make_more_files.py` which:

- Requests GPT-generated realistic fake sensitive file names
- Creates 1–5 fake files with believable names
- Adds a new `sys_####` subfolder to deepen the honeypot maze

---

## Step 6: Review Activity Logs

To view activity logs:

```bash
sudo ausearch -k honeypot_files
```

To export logs to a file:

```bash
sudo ausearch -k honeypot_files > honeypot_raw.log
```

## Notes

- Ensure you have internet access and a valid OpenAI API key for GPT functionality.
