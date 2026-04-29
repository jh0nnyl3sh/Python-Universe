# 🛡️ Day 86: Path Traversal Solver (Stack / LIFO Architecture)

> **⚠️ EDUCATIONAL PURPOSE ONLY:**
> This script is a proof-of-concept demonstrating how operating systems and Web Application Firewalls (WAF) parse directory paths to mitigate Directory Traversal (LFI) attacks.

This project focuses on core Computer Science principles, specifically the **Stack** data structure and its **LIFO (Last In, First Out)** mechanism. 

### 🧠 The Concept & Architecture
When navigating directories or parsing potentially malicious payloads like `../../../etc/passwd`, backend systems rely on a Stack architecture to determine the absolute path.

1. **Split Operation:** The raw string is split by `/` delimiter.
2. **Push (Append):** Normal directory names are pushed onto the top of the Stack.
3. **Pop:** The `..` (parent directory) command triggers a `pop` operation, removing the most recently added directory from the Stack (LIFO rule).
4. **Defensive Check:** A crucial `if stack:` check prevents `IndexError` exceptions when an attacker attempts to traverse beyond the root directory.
5. **Join Operation:** The finalized Stack is rebuilt into a standardized Unix path.

### 🚀 Usage

Execute the solver directly from your terminal:
```bash
python path_solver.py
```

### 📊 Tactical Output Example

```text
[*] Gelen Orijinal Path: var/www/html/../../log/apache2/../nginx
[+] İşlem Sonrası Stack: ['var', 'log', 'nginx']
[+] Çözülmüş Nihai Path: /var/log/nginx
```

---
*Developed as part of the 100 Days of Python Challenge (Day 86 - Red Team Computer Science).*